# # 字面量：整形（int）浮点型（float）字符串（str）布尔型（bool）空值（NoneType）
# print(100) #整形（int）
# print(3.14) #浮点型（float）
# print("Hello, World!") #字符串（str）
# print(True) #布尔型（bool），首字母大写
# print(False) #布尔型（bool），首字母大写
# print(None) #空值（NoneType），首字母大写
#    #布尔型在涉及数学运算时，True为1，False为0
# print(True + 1) #输出2    
# print(False - 1) #输出-1


# # 变量,python是动态类型语言，变量不需要声明类型，变量名可以随意命名，但不能以数字开头，不能使用关键字，不能使用空格，不能使用特殊符号（除了下划线_），区分大小写
# num = 100
# print(num) #输出100
# num = num + 1
# print(num) #输出101
# num = 'ok'
# print(num) #输出'ok'


# # 案例1
# a,b = 10,20
# c = a
# a = b
# b = c
# print(a,b) #输出20 10

# # 案例2,将a,b,c的值分别赋给c,a,b
# a,b,c = 100,200,300
# d = a
# a = b
# b = c
# c = d
# print(a,b,c)



#常见数据类型,type(),isinstance()
# print('hello')
# print(type('hello'))
# print(type(True))
# print(isinstance(-100,int))
# print(isinstance(-100,bool))
# print(isinstance(-100,float))


# # 转义字符
# print('it's verygood') #错误，需要转义
# print('it\'s verygood') #转义
# print('\t123\n\t456')





#字符串拼接
# s1 = 'hello'
# s3 = 'world'
# print('python: ' + s1 + ' '+ s3) #字符串拼接

# # 案例0
# name = 'fly'
# age = 20
# major = '信息安全'
# hobby = '小说'
# print('大家好，我是' + name + ',今年' + str(age) + '岁，学习的专业是' + major + ',爱好是' + hobby)




# # 输入输出
# name = input('请输入你的名字：')
# age = input('请输入你的年龄：')
# print(f'您的姓名是{name}，年龄为{age}')





# # 案例
# password = input('请输入您的密码：')
# num = int(input('请输入取款金额'))
# total = 10000
# print(f'剩余余额为:{total-num}')

# # 案例1
# num1 = int(input("请输入数字1："))
# num2 = int(input("请输入数字2："))
# print(f'和为：{num1 + num2}')

# # 算术运算符
# x = int(input('请输入数字1：'))
# y = int(input('请输入数字2：'))
# print(f'和为：{x + y}')
# print(f'差为：{x - y}')





#逻辑运算符
num = int(input('请输入一个整数：'))
print(f'{num}在10-20之间:',num > 10 and num < 20)
print(f'{num}在10-20之间:',10 < num <20)#链式