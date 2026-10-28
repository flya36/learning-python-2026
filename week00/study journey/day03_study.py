# #if条件判断
# score = 596
# if score > 680:
#     print('清华欢迎你')
# print('-----------')





# #案例：输入账号密码登录
# id = input('请输入账号：')
# password = input('请输入密码：')
# if id == '1888888' and password == '88888':
#     print('欢迎登陆')
# else:
#     print('账号密码错误')




# #判断是否是闰年
# year = int(input('请输入年份：'))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
#     print(f'{year}是闰年')
# else:
#     print(f'{year}是平年')





# #判断数字是奇数还是偶数
# num = int(input('请输入数字：'))
# if num % 2 == 0:
#     print(f'{num}是偶数')
# else:
#     print(f'{num}是奇数')






# #判断用户是否成年
# age = int(input('请输入您的年龄：'))
# if age >= 18:
#     print('您已成年')
# else:
#     print('您未成年')





# #判断数字是正负数还是0
# num = int(input('请输入数字：'))
# if num < 0:
#     print(f'{num}是负数')
# elif num > 0:
#     print(f'{num}是正数')
# else:
#     print(f'{num}是0')




# #根据用户名登陆系统
# name = input('请输入用户名：')
# password = input('请输入密码：')
# if name =='admin' and password == '666888':
#     print('登陆成功')
# elif name == 'root' and password == '547527':
#     print('登陆成功')
# elif name == 'zhangsan' and password == '123456':
#     print('登陆成功')
# else:
#     print('登陆失败,账号密码错误')




# #购物折扣
# amount = float(input('请输入购物金额：'))
# if amount >= 500:
#     print('实际应付：',amount*0.8)
# elif 300 <= amount < 500:
#     print('实际应付：',amount*0.9)
# elif 100 <= amount < 300:
#     print('实际应付：',amount*0.95)
# else:
#     print('无折扣')



# #用电
# elc = float(input('请输入用电度数：'))
# if 0 < elc < 2880:
#     print('电费为：',round(elc*0.4883,2))
# elif 2880 <= elc <= 4800:
#     print('电费为：',round(2880*0.4883+(elc-2880)*0.5383,2))
# elif elc > 4800:
#     print('电费为：',round(2880*0.4883+(4800-2880)*0.5383+(elc-4800)*0.7883,2))
# else:
#     print('输入错误')    







# day = input('请输入星期几：')
# match day:
#     case '1':
#         print()
#     case '2':
#         print()
#     case _:
#         print()





# #计算器
# num1 = float(input('请输入第一个数：'))
# num2 = float(input('请输入第二个数：'))
# oper = input('请输入运算符：')
# match oper:
#     case '+':
#         print(f'{num1}+{num2} = {num1+num2}')
#     case '-':
#         print(f'{num1}-{num2} = {num1-num2}')
#     case '*':
#         print(f'{num1}*{num2} = {num1*num2}')
#     case '/' if num2 != 0:
#         print(f'{num1}/{num2} = {num1/num2}')
#     case _:
#         print('输入错误')




# #简单游戏指令系统
# command = input('请输入指令：')
# match command:
#     case '上'|'w'|'W':
#         print('角色向上移动')
#     case '下'|'s'|'S':
#         print('角色向下移动')
#     case '左'|'a'|'A':
#         print('角色向左移动')
#     case '右'|'d'|'D':
#         print('角色向右移动')
#     case '跳'|' ':
#         print('角色跳跃')
#     case '攻击'|'j'|'J':
#         print('角色发动攻击')
#     case '退出'|'esc'|'ESC':
#         print('角色退出游戏')
#     case _:
#         print('指令错误')




# #while循环
# i = 0
# while i < 10:
#     print('我爱python')
#     i += 1




# #1-100之间所有偶数之和
# sum = 0
# i = 1
# while i < 101:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(f'1-100之间所有偶数之和为：{sum}')





# #1-100之间所有奇数之和
# sum = 0
# for i in range(1,101,2):
#     sum += i
# print(f'1-100之间所有奇数和为：{sum}')



# #打印长方形
# m = int(input('请输入长度'))
# n = int(input('请输入宽度'))
# for i in range(n):
#     for j in range(m):
#         print('*',end=' ')
#     print()



# #打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={i*j}',end='\t')
#     print()


# 打印等腰直角三角形
# h = int(input('请输入三角形的高度：'))
# for i in range(0,h):
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print()



# # 根据数字打印数字金字塔
# n = int(input('请输入数字：'))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(j+1,end=' ')
#     print()



# #打印国际象棋
# for i in range(1,9):
#     for j in range(1,9):
#         if (i+j) % 2 ==1:
#             print('◽',end='')
#         else:
#             print('◾',end='')
#     print()





# #练习
# i = 0
# while True:
#     name = input('请输入用户名：')
#     password = input('请输入密码：')
#     if name == 'admin' and password == '666888':
#         print('欢迎登陆')
#         break
#     elif name == 'zhangsan' and password == '123456':
#         print('欢迎登陆')
#         break
#     elif name == 'taoge' and password == '888666':
#         print('欢迎登陆')
#         break
#     else:
#         i = i+1
#         if i >= 5:
#             print('输入错误五次，不允许操作')
#             break




# #猜随机数
# import random
# random_num = random.randint(1,100)
# while True:
#     num = int(input('请输入数字：'))
#     if num > random_num:
#         print('数字大了')
#     elif num < random_num:
#         print('数字小了')
#     else:
#         print('恭喜猜对')
#         break





# #1-1000所有5的倍数数字累加
# sum = 0
# for i in range(0,1001,5):
#     sum += i
# print('1-1000所有5的倍数数字累加和为：',sum)



#统计akiwksjakdiklowiqaaamnvbamvaxnsjdsjkaaxkjd中a，k多少个
s = 'akiwksjakdiklowiqaaamnvbamvaxnsjdsjkaaxkjd'
sum1,sum2 = 0,0
for i in s:
    if i =="a":
        sum1 += 1
    elif i == 'k':
        sum2 += 1
print(f'a有{sum1}个，b有{sum2}个')