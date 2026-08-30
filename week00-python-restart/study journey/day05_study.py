# #列表

# #定义列表
# list1 = [1,2,3,4,5,6,7,8,9]
# print(type(list1))

# #获取查看
# print(list1[0],list1[-9])

# # 修改
# list1[2] = 3
# print(list1[2])

# #指定索引超出范围会报错：indexerror:list assignment index out of range

# #删除第3个元素
# del list1[2]
# print(list1)

# #切片操作[开始索引：结束索引：步长]
# print(list1[0:5:1])

# #列表常用方法（添加（append），插入（insert），删除（remove，pop），排序（sort），翻转（reverse））
# s = [1,2,3,4,5,6]
# # 在末尾添加元素7 append
# s.append(7)
# # 在第一个元素前插入元素0 insert
# s.insert(0,0)
# #删除元素6 remove
# s.remove(6)
# #删除第7个元素 pop
# s.pop(6)
# #对列表进行排序 sort
# s.sort()
# # 翻转 reverse
# s.reverse()
# print(s)

# #案例1:对输入的十个数字进行排序，输出最大值，最小值，平均值，sum()求和
# num_list = []
# for i in range(10):
#     num = int(input('请输入数字'))
#     num_list.append(num)
# num_list.sort()
# print(f'最小值：{num_list[0]},最大值：{num_list[-1]},平均值：{sum(num_list)/len(num_list)}')

# # 案例2：合并两个列表并去重
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# for i in num_list2:
#     num_list1.append(i)
# print('合并后的列表：',num_list1)
# new_list = []
# for num in num_list1:
#     if num not in new_list:
#         new_list.append(num)
# print('去重后的列表：',new_list)

# # 案例2（简化1）：合并两个列表并去重
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# num_list = []
# #解包：将容器内的值解开为一个个单独元素   组包：将多个值合并到一个容器
# num_list = [*num_list1,*num_list2]
# print('合并后的列表：',num_list)
# new_list = []
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print('去重后的列表：',new_list)

# # 案例2（简化2）：合并两个列表并去重
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# num_list = num_list1 + num_list2
# print('合并后的列表：',num_list)
# new_list = []
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print('去重后的列表：',new_list)

# #案例3：生成1-20的平方列表
# num_list = [i**2 for i in range(1,21)]
# print(num_list)

# #案例4：从一个数字列表中提取所有的偶数并计算其平方，组成一个新的列表
# num_list = [31,52,12,65,41,76,41,245,32,10]
# new_list = [i**2 for i in num_list if i % 2 ==0]
# print(new_list)

# # 需求1 合并列表去重排序
# list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
# list2 = ['X','Z','T','Y','D','E','F','G']
# list3 = ['W','A','S','D']
# list4 = list1 + list2 + list3
# new_list = []
# for i in list4:
#     if i not in new_list:
#         new_list.append(i)
# new_list.sort()
# print(new_list)

# # 需求2：将能被3，5整除的元素提出并获取平方，组成新列表
# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# list2 = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
# print(list2)

# # 需求3：将正数提取出来组成新列表
# list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
# new_list = []
# new_list = [i for i in list1 if i > 0]
# print(new_list)

# #字符串的基本操作 -->不可变性，可迭代性，有序性
# s = 'python'
# print(s[-4])#反向索引

# # 字符串的常用方法
# s = 'Hello-Python-Hello-Python-Hello-Python'
# #查找：find，count
# # 查找第一次出现'-'的索引位置
# index=s.find('-')
# print(index)
# # 查找o出现的次数
# c = s.count('o')
# print(c)
# #将字符串全部转为大写或小写-->upper(),lower()
# s_u = s.upper()
# s_l = s.lower()
# print(s_u)
# print(s_l)
# # 切割字符串-->split()
# s_s = s.split('-')
# print(s_s)
# #去除字符串中两端空白或两端指定字符-->strip
# s_s = s.strip('H')
# print(s_s)
# # 将字符串中指定字符替换成其它字符-->replace()
# s_r = s.replace('H','h')
# print(s_r)

# #案例1：判断邮箱格式是否正确（至少有一个.和只有一个@）
# email = input('请输入您的邮箱')
# if email.count('@') == 1 and email.count('.') >= 1:
#     print('邮箱格式正确')
# else:
#     print('邮箱格式错误')

# #方式二：
# email = input('请输入您的邮箱')
# if email.count('@') == 1 and '.' in email:
#     print('True')
# else:
#     print('False')

# # 练习1:判断是否是回文结构
# s = input('请输入:')
# if s == s[::-1]:
#     print('是回文结构')
# else:
#     print('不是回文结构')

# 练习二
# list1 = []
# for i in range(10):
#     s = input('请输入字符串')
#     list1.append(s[-1::-1].upper())

# for i in list1:
#     print(i)

# #元组的基本操作-->元素不可修改，有序，可重复
# #定义
# t1 = (1,2,1,5,2,3,7,3,8)
# #索引访问
# print(t1[-1])
# print(t1[0])
# #切片
# print(t1[::-1])
# #统计某元素出现次数
# print(t1.count(1))
# #获取元素第一个索引位置
# print(t1.index(2))

# 组包操作
t1 = (2,13,421,33,14,63,15)
# #解包操作
# a,b,c,d,e,f,g = t1  #基础解包操作
# print(a,b,c,d,e,f,g)
# first,*middle,last = t1    #扩展解包(*收集元组剩余所有元素，封装到列表中)
# print(first,last)
# print(middle,type(middle))

# #a=10,b=20，将ab值互换
# a = 10
# b = 20
# #先组包再解包
# a,b = (b,a)
# print(a)
# print(b)

# # a=100,b=200,c=300,将abc赋值给cab
# a,b,c = 100,200,300
# c,a,b = a,b,c
# print(a,b,c)

'''根据提供的学生成绩单,完成如下需求:
1. 计算每个学生的总分、各科平均分,然后一并输出出来。
2. 统计各科成绩的最低分、最高分、平均分,并输出。
3. 查找成绩优秀(平均分大于90)的学生,并输出。
'''
students = (
('S001','王林',85,92,78),
('S002','李慕婉',92,88,95),
('S003','十三',78,85,82),
('S004','曾牛',88,79,91),
('S005','周轶',95,96,89),
('S006','王卓',76,82,77),
('S007','红蝶',89,91,94),
('S008','徐立国',75,69,82),
('S009','许木',86,89,98),
('S010','通天',66,59,72)
)
# 计算每个学生的总分、平均分,然后一并输出出来
print('姓名\t总分\t平均分\t')
for s in students:
    total_score = s[2]+s[3]+s[4]
    ave = total_score/3
    print(f'{s[1]}\t{total_score}\t {ave:.1f}')
# 统计各科成绩的最低分、最高分、平均分,并输出。
ch_score = [s[2] for s in students]
m_score = [s[3] for s in students]
en_score = [s[4] for s in students]
print(f'语文：最高分{max(ch_score)}，最低分{min(ch_score)}，平均分：{sum(ch_score)/len(ch_score)}')
print(f'数学：最高分{max(m_score)}，最低分{min(m_score)}，平均分：{sum(m_score)/len(m_score)}')
print(f'英语：最高分{max(en_score)}，最低分{min(en_score)}，平均分：{sum(en_score)/len(en_score)}')
# 查找成绩优秀(平均分大于90)的学生,并输出。
for s in students:
    total_score = s[2]+s[3]+s[4]
    ave = total_score/3
    if ave > 90:
        print(f'成绩优秀学生：{s[1]}')