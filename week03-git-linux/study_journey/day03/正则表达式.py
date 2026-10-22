import re

s1 = '18809090000 是我的手机号，你记住了吗？我的另一个手机号是 1880008888，两个 QQ 号分别是 155998992 和 188090929321987,邮箱是3436247611@qq.com'
s2 = ' 我的手机号是 18809090000，你记住了吗？我的另一个手机号是 1880008888，两个 QQ 号分别是 155998992 和 188090929321987'

# # match - 从开头进行匹配，只匹配一个匹配项-->返回match对象
# # group()-->返回结果
# # span()-->返回匹配项的索引
# # start()-->返回匹配项的开始索引
# # end()-->返回匹配项的结尾索引
# res1 = re.match(r'1[3-9]\d{9}',s1)
# # search - 从 anywhere 匹配-->返回match对象
# res2 = re.search(r'1[3-9]\d{9}',s2)
# # findall - 找到所有匹配项-->返回list
# res3 = re.findall(r'1[3-9]\d{9}',s1)
# print(res1.group(),res2.group(),res3)

# print(re.findall(r'188.*',s1))   #.*-->任意字符
# print(re.findall(r'188.?',s1))   #？-->至多出现一次
# print(re.findall(r'188.+',s1))   #+-->至少出现一次

# print(re.findall(r'1\d{8}',s1))     #{}-->指定次数,出现多少次
# print(re.findall(r'155\d{1,6}',s1)) #{1,6}-->至少出现一次，至多出现六次
# print(re.findall(r'155\d{6,}',s1))  #{6,}-->至少出现六次

# print(re.findall(r'1[38]\d{8}',s1))     #[38]-->匹配3或8
# print(re.findall(r'1[^38]\d{7}',s1))    #[^38]-->匹配非3或8
# print(re.findall(r'1[3-9]\d{7}',s1))    #[3-9]-->匹配3到9
# print(re.findall(r'^1[3-9]\d{7}',s1))   #^-->匹配开头,只匹配一个匹配项
# print(re.findall(r'1[3-9]\d{7}$',s1))   #$-->匹配结尾

# print(re.findall(r'\w+@\w+\.\w+',s1))
# print(re.findall(r'\w+@\w+\.\w+',s1,re.ASCII))

s3 = '现在是2026-10-17 22:34:05.'
print(re.findall(r'\d{4}-\d{2}-\d{2}',s3))
print(re.findall(r'(\d{4})-(\d{2})-(\d{2})',s3))