# # 集合--->无序，不可重复，可以修改
# # 定义
# s1 = {2,32,14,24,51,21,12,51}
# print(s1)
# # 定义空集合
# s2 = set()

# #set常用方法
# s1 = {1,2,3,4,5,6,7,8,9}
# print(s1)
# #添加10
# s1.add(10)
# print(s1)
# #删除6
# s1.remove(6)
# print(s1)
# #随机删除
# s1.pop()
# print(s1)
# s2 = {1,2,3,4,5,6,7,8,9,10,11,12}
# #求s1关于s2的差集
# print(s1.difference(s2))
# print(s2.difference(s1))
# # 求并集
# print(s1.union(s2))
# # 求交集
# print(s1.intersection(s2))

# '''案例1 根据提供的班级学生的选课情况，完成如下需求：
# 1.找出同时选修了法语和艺术的学生
# 2.找出同时选修了所有四门课程的学生
# 3.找出选修了足球，但是没有选修篮球的学生
# 4.统计每一个学生选修的课程数量
# '''
# # 选修足球学生名单
# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# # 选修篮球学生名单
# basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# # 选修法语学生名单
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# # 选修艺术学生名单
# art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
# #1.找出同时选修了法语和艺术的学生
# #方式一：
# fa_set = french_set.intersection(art_set)
# print(f'同时选修了法语和艺术的学生：{fa_set}')
# # 方式二：&-->求交集（与）
# fa_set2 = french_set & art_set
# print(f'同时选修了法语和艺术的学生：{fa_set2}')
# # 找出同时选修了所有四门课程的学生
# all_set = football_set & basketball_set & french_set & art_set
# print(f'同时选修了所有四门课程的学生:{all_set}')
# # 找出选修了足球，但是没有选修篮球的学生 差集（difference -）
# fb_set = football_set.difference(basketball_set)
# print(f'选修了足球，但是没有选修篮球的学生:{fb_set}')
# # 差集：-
# fb_set1 = football_set - basketball_set
# print(f'选修了足球，但是没有选修篮球的学生:{fb_set1}')
# #集合推导式-->{ for s in set 条件}
# fb_set2 = {s for s in football_set if s not in basketball_set}
# print(f'选修了足球，但是没有选修篮球的学生:{fb_set2}')
# # 统计每一个学生选修的课程数量
# # 并集 union |
# total_set = football_set.union(basketball_set).union(french_set).union(art_set)
# total_set1 = football_set | basketball_set | french_set | art_set
# print(f'所有学生:{total_set}')
# print(f'所有学生:{total_set1}')
# total_list = [*football_set,*basketball_set,*french_set,*art_set]
# for s in total_set:
#     print(f'学生{s}修{total_list.count(s)}课程')



# #字典dict
# # 定义
# dict1 = {'王琳':680,'fly':700}
# print(dict1)
# # 重复，后面的值覆盖前面的值
# dict1 = {'王琳':680,'fly':700,'王琳':580}
# print(dict1)
# # 查找
# print(f'王琳的成绩：{dict1['王琳']}')
# # 修改
# dict1['fly'] = 596
# print(dict1)

# 常用操作
dict1 = {'王立':{'语文':500,'数学':21},'韩立':{'语文':520,'数学':321},'风':{'语文':540,'数学':12}}
# print(dict1)
# # 添加贤者：560
# dict1['贤者'] = 560
# # 修改捷风：560
# dict1['捷风'] = 560
# # 删除王立
# del dict1['王立']
# print(dict1)
# score = dict1.pop('王立')
# print(dict1,score)
# # 查询贤者
# score = dict1['贤者']
# print(score)
# print(dict1.get('贤者'))
# 查询所有学生姓名和成绩
print(dict1.values())
print(dict1.keys())
print(dict1.items())
# # 遍历
# # # 方式一
# # for k in dict1.keys():
# #     print(f'{k}:{dict1[k]}')
# #     print(f'{k}:{dict1.get(k)}')
# # 方式二
# for k,v in dict1.items():
#     print(f'{k}:{v}')



# 案例
