# SQL 速查页（CourseMate 真实表）

> 表结构：
> - `course(id, name UNIQUE, description, created_at)`
> - `document(id, course_id FK→course.id RESTRICT, filename, file_type, file_path, file_size, created_at)`
> - `chunk(id, document_id FK→document.id, content, page_number, chunk_order, created_at)`
>
> 用法：想不起来怎么写时先看这里，再 `explain` 验证走没走索引。

## 1. SELECT + WHERE + 分页（列表查询）

```sql
select id, name, created_at
from course
where description is not null
order by id
limit 3 offset 3;
```

- **什么时候用**：列表接口。`offset = (page - 1) * limit`。
- **必须记**：不写 `order by`，分页顺序不稳定（同一页可能重复或漏行）。
- **踩过的坑**：`limit 3 offset 3` 是"跳过前 3 条，再取 3 条"（第 4—6 条），不是"取第 3 到第 6 条"。

## 2. LEFT JOIN（一对多统计，父行不能丢）

```sql
-- 每门课的文档数：没文档的课程也要显示 0
select c.id, c.name, count(d.id) as doc_count
from course c
left join document d on c.id = d.course_id
group by c.id, c.name
order by c.id;
```

- **什么时候用**：父子表统计，父表所有行都必须出现（哪怕子表是 0）。
- **必须记**：写 `count(d.id)` 而不是 `count(*)`。`count(*)` 会把"左连接补出来的 NULL 行"也数进去，没文档的课程会变成 1。
- **踩过的坑（`on` vs `where`）**：

```sql
-- 版本 A：过滤放在 ON → 课程行保留，大文件匹配不上则计数为 0
select c.id, c.name, count(d.id)
from course c left join document d
  on c.id = d.course_id and d.file_size > 1048576
group by c.id, c.name;

-- 版本 B：过滤放在 WHERE → 没有大文件的课程被整行过滤掉（LEFT 变 INNER）
select c.id, c.name, count(d.id)
from course c left join document d on c.id = d.course_id
where d.file_size > 1048576
group by c.id, c.name;
```

## 3. 聚合 + GROUP BY + HAVING（分组后再筛选）

```sql
-- 只看"有文档"的课程，并汇总文件总大小
select c.id, c.name,
       sum(d.file_size) as total_size,
       count(d.id)     as doc_count
from course c
left join document d on c.id = d.course_id
group by c.id, c.name
having count(d.id) >= 1;
```

- **什么时候用**：按维度汇总；且要对"汇总出来的值"再筛。
- **必须记**：`WHERE` 在分组**前**执行——那时还没有"组"，所以 `WHERE` 里不能用 `count` / `sum`；要按聚合值筛只能用 `HAVING`。
- **必须记 2**：`SUM` 对空组返回 `NULL`，`COUNT` 返回 `0`。想让空组显示 0：`ifnull(sum(d.file_size), 0)`。
- **踩过的坑**：初版漏写 `sum()` 和 `group by`，直接列 `d.file_size` → 结果是一堆未聚合的原始行。

## 4. 索引与 EXPLAIN（判断到底走不走索引）

```sql
show index from course;                                          -- 看已有索引
show index from document;

explain select * from course where id = 2;                       -- 主键 → Index lookup
explain select * from course where name = '数据结构';             -- 唯一索引 → Index lookup
explain select * from course where description = '大三专业课';     -- 无索引 → Table scan
```

树形 EXPLAIN 的读法：**从下往上**。

```
-> Filter: (course.description = '大三专业课')  (cost=0.85 rows=1)
    -> Table scan on course  (cost=0.85 rows=6)
```

- 出现 `Table scan on X` = 全表扫描（没有可用索引）
- 出现 `Index lookup` / `Index range scan` = 走了索引
- 老式表格格式：`explain format=traditional select ...`，看 `type` 列——`ALL` 就是全表扫描，`key` 列是实际用的索引名（NULL 表示没用）

- **什么时候用**：慢查询先 `explain`，不要猜。
- **必须记**：索引是"**给读加速、给写拖后腿**"。每次 `INSERT` 都要把新值插进 B+ 树（找位置、可能页分裂），所以写多的表别乱加索引。
- **建索引决策**：

| 场景 | 该建吗 |
| --- | --- |
| 常在 `where` / `order by` / `join on` 出现的列 | 建 |
| 区分度高（id / 手机号 / 学号，值几乎不重复） | 建 |
| 区分度低（性别、状态只有 2—3 个值） | 不建 |
| 写远多于读的表（日志、埋点） | 尽量少建 |

- **本项目现状**：`course` 有 `PRIMARY(id)` + `name` 唯一索引；`document` 有 `PRIMARY(id)` + `course_id` 外键索引；`description` 无索引 → 查它必然 Table scan。

## 附：三层删除顺序（外键 RESTRICT）

```sql
delete from chunk    where document_id = ?;   -- 1. 最底层先删
delete from document where id = ?;            -- 2. 再删文档
delete from course   where id = ?;            -- 3. 最后删课程
```

顺序反了立刻报：

```
Error Code: 1451
Cannot delete or update a parent row: a foreign key constraint fails
(`coursemate`.`document`, CONSTRAINT `document_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`))
```

接口层对应行为：`DELETE /courses/{id}` 在课程下还有文档时返回 **409**（捕获 `IntegrityError` → `rollback` → 业务提示），而不是 500。
