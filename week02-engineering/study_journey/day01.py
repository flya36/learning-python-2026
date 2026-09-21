# # 定义类
# class Car:
#     pass

# # 创建对象
# c1 = Car()
# # 为对象添加属性
# c1.color = 'red'
# c1.brand = 'xiaomi'
# c1.name = 'yu7'
# c1.price = 300000
# print(c1.__dict__)
# print(c1.brand)

# 定义类
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print('对象初始化完毕，属性已添加')
# c1 = Car('red','xiaomi','yu7',300000)
# print(c1.__dict__)
# print(c1)

# # 实例方法
# class Car:
#     # 类属性
#     wheel = 4
#     tax_rate = 0.1
#     # 实例属性
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print('对象初始化完毕，属性已添加')
#     def total_cost(self,discount,rate):
#         return self.price * (discount + rate)
#     # 魔法方法-->__str__/__eq__/__lt__/__le__/__gt__/__ge__
#     def __str__(self):
#         return f'{self.color} {self.brand} {self.name} {self.price}'
#     def __eq__(self, other):
#         return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
#     def __lt__(self, other):
#         return self.price < other.price
# c1 = Car('red','xiaomi','yu7',300000)
# c2 = Car('red','xiaomi','yu7',300000)
# # total_cost = c1.total_cost(0.8,0.1)
# # print(total_cost)

# # 魔法方法-->__str__/__eq__/__lt__/__le__/__gt__/__ge__
# print(c1)
# print(c1==c2)
# print(c1<c2)

# # 实例属性和类属性
# print(c1.brand)
# print(c1.wheel)     #先查找实例属性，实例属性没有再查找类属性
# print(Car.wheel)

# '''
# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
# 1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
# 2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
# 3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
# 4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
# 5. 展示全部学生成绩：展示出系统中所有学生的成绩
# '''
# class Student:
#     def __init__(self,name,chinese,math,english):
#         self.name = name
#         self.chinese = chinese
#         self.math = math 
#         self.english = english
#     # 查询指定学生成绩
#     def __str__(self):
#         return f'姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分{self.chinese + self.math + self.english}'
#     def update_student(self,chinese=None,math=None,english=None):
#         if chinese is not None:
#             self.chinese = chinese
#         if math is not None:
#             self.math = math
#         if english is not None:
#             self.english = english
# class Edumanagement:
#     def __init__(self):
#         self.student_list = []
#     # 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
#     def add_student(self):
#         name = input('请输入要添加的学生姓名：')
#         for s in self.student_list:
#             if s.name == name:
#                 print('该学生已存在，添加失败！')
#                 return 
#         chinese = int(input('请输入学生语文成绩：'))
#         math = int(input('请输入学生数学成绩：'))
#         english = int(input('请输入学生英语成绩：'))
#         if 0 <= chinese <=100 and 0 <= math <= 100 and 0 <= english <= 100:
#             stu = Student(name,chinese,math,english)
#             self.student_list.append(stu)
#             print('学生信息添加成功')
#         else:
#             print('输入成绩非法,不在0-100之间')
#     # 修改学生成绩
#     def uodate_student_info(self):
#         name = input('请输入要修改的学生姓名：')
#         for s in self.student_list:
#             if s.name == name:
#                 chinese = int(input('请输入要修改的语文成绩：'))
#                 math = int(input('请输入要修改的数学成绩：'))
#                 english = int(input('请输入要修改的英语成绩：'))
#                 s.update_student(chinese,math,english)
#                 print('学生成绩修改成功')
#                 return 
#         print('姓名输入错误，学生不存在！')
#     # 删除学生成绩
#     def del_student(self):
#         name = input('请输入要删除的学生姓名：')
#         for s in self.student_list:
#             if s.name == name:
#                 self.student_list.remove(s)
#                 print('学生成绩删除成功')
#                 return
#         print('姓名输入错误，学生不存在')
#     # 查询指定学生成绩
#     def find_student(self):
#         name = input('请输入要查询的学生姓名：')
#         for s in self.student_list:
#             if s.name == name:
#                 print(s)
#                 return 
#         print('姓名输入错误，学生不存在')
#     # 展示全部学生成绩
#     def show_student(self):
#         for s in self.student_list:
#             print(s)
# edumanagement = Edumanagement()
# print('欢迎进入教务管理系统')
# print()
# while True:
#     print('##############################################################################################')
#     print('#  1.添加学生成绩 2.修改学生成绩 3.删除学生成绩 4.查询指定学生成绩 5.展示全部学生成绩 6.退出 #')
#     print('##############################################################################################')
#     choice = input('请选择操作数字：')
#     match choice:
#         case '1':
#             edumanagement.add_student()
#         case '2':
#             edumanagement.uodate_student_info()
#         case '3':
#             edumanagement.del_student()
#         case '4':
#             edumanagement.find_student()
#         case '5':
#             edumanagement.show_student()
#         case '6':
#             break
#         case _:
#             print('输入数字非法，请重新输入')


'''
采用面向对象的编程思想，开发一个**购物车管理系统**，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称:xxx,商品价格:xxx,商品数量:xxx"。
5. 退出购物车
'''
class Goods:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num
    # 查询购物车-->"商品名称:xxx,商品价格:xxx,商品数量:xxx"
    def __str__(self):
        return f'商品名称:{self.name},商品价格:{self.price},商品数量:{self.num}'
    # 修改商品信息
    def update_goods(self,price = None,num = None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num
class ShoppingCartManagement:
    def __init__(self):
        self.shopping_cart = []
    # 添加购物车
    def add_goods(self):
        name = input('请输入商品名称：')
        for g in self.shopping_cart:
            if g.name == name:
                print('商品信息已存在')
                return 
        price = int(input('请输入商品价格：'))
        num = int(input('请输入商品数量：'))
        goods = Goods(name,price,num)
        self.shopping_cart.append(goods)
        print('商品信息添加成功')
    # 修改购物车
    def update_shopping_cart(self):
        name = input('请输入要修改的商品名称：')
        for g in self.shopping_cart:
            if name == g.name:
                price = input('请输入修改后的商品价格：')
                num = input('请输入修改后的商品数量：')
                g.update_goods(price,num)
                print('商品信息修改成功')
                return 
        print('商品信息不存在')
    # 删除购物车
    def delete_shopping_cart(self):
        name = input('请输入要删除的商品名称：')
        for g in self.shopping_cart:
            if name == g.name:
                self.shopping_cart.remove(g)
                print('商品删除成功')
                return 
        print('要删除的商品信息不存在')
    # 查询购物车
    def find_shopping_cart(self):
        if not self.shopping_cart:
            print("购物车为空！")
            return 
        for g in self.shopping_cart:
            print(g)