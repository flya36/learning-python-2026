# # 封装
# class Car:
#     def __init__(self,brand,model,color,owner):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.__owner = owner
#     def output(self):
#         print(f'{self.__owner}:{self.brand},{self.model},{self.color}')
#     def __privite(self):
#         print('这是私有方法')
#     def get_owner(self):
#         return self.__owner[0:1] + '**'
# c1 = Car('xiaomi','yu7','black','fly')
# print(c1.color)
# print(c1.model)
# c1.output()
# print(c1.get_owner())

# # 继承
# class Car:
#     def __init__(self,brand,model,color,owner):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.__owner = owner
#     def output(self):
#         print(f'{self.brand},{self.model},{self.color}')
#     def __privite(self):
#         print('这是私有方法')
#     def get_owner(self):
#         return self.__owner[0:1] + '**'
# class Fuelcar(Car):
#     pass
# class ElectricCar(Car):
#     pass
# # if __name__ == '__main__':
# #     c1 = ElectricCar('xiaomi','yu7','black','fly')
# #     print(c1.get_owner())
# #     print(c1.model)
# #     c1._ElectricCar__privite()

# # 多继承，有顺序，同一函数名，在前的类优先使用，可用__mro__查看顺序
# class XiaoMiAiDriving:
#     def __init__(self,version='V1.0'):
#         self.version = version
#     def run(self):
#         print('使用小米AI智能驾驶系统{self.version}正在驾驶...')
# class xiaomi(Car,XiaoMiAiDriving):
#             def __init__(self, brand, model, color, owner,version='V0.1'):
#                 super().__init__(brand, model, color, owner)
#                 XiaoMiAiDriving.__init__(self,version)
# if __name__=='__main__':
#     #  c = xiaomi()
#      print(xiaomi.__mro__)

# # 案例一
# '''
# 某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。系统中有两种类型的会员：普通会员和 VIP 会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。

# 核心功能：
# 1. 会员登录：会员通过卡号和密码登录系统
# 2. 借书：会员可以借阅库存中有余量的图书
# 3. 还书：会员可以归还借阅的图书
# 4. 查看我的借阅：展示当前会员已经借阅的图书列表
# 5. 退出系统

# 借阅规则：
# 1. 普通会员最多可借 3 本
# 2. VIP 会员最多可借 6+VIP 等级 (VIP 等级，默认为 1)

# 注意：
# 1. 登录成功（卡号和密码均正确）后，才可以访问该系统
# 2. 图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书
# '''
# import json
# class Book:
#     def __init__(self,book_id,title,author,total_num):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.total_num = total_num
#         self.__available_num = total_num
#     def borrow_book(self):  #借书
#         if self.__available_num > 0:
#             self.__available_num -= 1
#             return True
#         return False
#     def return_book(self):  #还书
#         self.__available_num += 1
#     def get_available_num(self):    #现有书籍数量
#         return self.__available_num
# from abc import ABC,abstractmethod
# # 会员类
# class Member(ABC):
#     def __init__(self,member_id,name,password):
#         self.member_id = member_id
#         self.name = name
#         self.__password = password
#         self.__borrowed_books = []  #借阅书籍列表
#     def borrow_book(self,book:Book):
#         # 判断会员借书是否到达最大数量
#         if len(self.__borrowed_books) >= self.get_max_books():
#             print('您的借阅书籍已达到最大限制')
#             return False
#         if book.borrow_book():
#             self.__borrowed_books.append(book)
#             print(f'{self.name}已成功借阅{book.title}')
#             return True
#         else:
#             print(f'{book.title}已被借完')
#             return False
#     def return_book(self,book:Book):
#         if book in self.__borrowed_books:
#             book.return_book()
#             self.__borrowed_books.remove(book)
#             print(f'{self.name}已成功归还书籍{book.title}')
#         else:
#             print(f'归还失败，没有借过{book.title}')
#     def get_password(self):
#         return self.__password
#     def get_borrowed_books(self):
#         return self.__borrowed_books
#     @abstractmethod
#     def get_max_books(self):
#         pass
# # 子类：普通会员
# class NormalMember(Member):
#     def get_max_books(self):
#             return 3
# class VipMember(Member):
#     def __init__(self, member_id, name, password,vip_level:int):
#         super().__init__(member_id, name, password)
#         self.vip_level = vip_level
#     def get_max_books(self):
#         return 6 + self.vip_level
# class LibrarySystem:
#     def __init__(self):
#         self.books = {}
#         self.members = {}
#         self.current_member:Member = None
#         # 加载数据（书籍/会员）
#         self.load_books_data()
#         self.load_members_data()
#     def load_books_data(self):
#         with open('data/books.json','r',encoding='utf-8') as f:
#             books = json.load(f)
#             for book in books:
#                 self.books[book['编号']] = Book(book['编号'],book['标题'],book['作者'],book['数量'])
#                 print('加载书籍数据成功')
#     def load_members_data(self):
#         with open('data/members.json','r',encoding='utf-8') as f:
#             members = json.load(f)
#             for member in members:
#                 if member['卡号'].startswith('V'):
#                     self.members[member['卡号']] = VipMember(member['卡号'],member['姓名'],member['密码'],member['会员等级'])
#                 elif member['卡号'].startswith('N'):
#                     self.members[member['卡号']] = NormalMember(member['卡号'],member['姓名'],member['密码'])
#                 print('加载会员数据成功')
#     # 登录功能
#     def login(self):
#         while True:
#             print('【登录】')
#             member_id = input('请输入会员卡号')
#             password = input('请输入会员密码')
#             if member_id not in self.members:
#                 print('登陆失败，会员不存在')
#                 continue
#             member = self.members[member_id]
#             if password != member.get_password():
#                 print('登陆失败，密码错误')
#                 continue
#             else:
#                 print(f'登陆成功，欢迎您{member.name}')
#                 self.current_member = member
#                 return True
#     def run(self):
#         if self.login():
#             while True:
#                 print('\n1.借阅图书')
#                 print('2.归还图书')
#                 print('3.查看借阅')
#                 print('4.退出系统')

#                 choice = input('请输入操作(1-4):')
#                 match choice:
#                     case '1':
#                         self.borrow_book()
#                     case '2':
#                         self.return_book()
#                     case '3':
#                         self.show_borrowed_book()
#                     case '4':
#                         return 
#                     case _:
#                         print('输入非法字符，请重新输入')
#     def borrow_book(self):
#         for book in self.books.values():
#             print(f'编号：{book.book_id}，标题：{book.title}，作者：{book.author}，总数：{book.total_num}，可用：{book.get_available_num()}')
#             book_id = input('请输入要借阅的图书编号：')
#             if book_id not in self.books:
#                 print('借阅失败，图书不存在')
#                 return
#             self.current_member.borrow_book(self.books[book_id])
#     def return_book(self):
#         borrowed_books = self.current_member.get_borrowed_books()
#         print('【已经借阅图书列表】')
#         for book in borrowed_books:
#             print(f'编号：{book.book_id}，标题：{book.title}')
#         book_id = input('请输入要归还图书编号：')
#         if book_id not in self.books:
#             print('还书失败，该图书不存在')
#             return
#         self.current_member.return_book(self.books[book_id])
#     def show_borrowed_book(self):
#         borrowed_books = self.current_member.get_borrowed_books()
#         if len(borrowed_books) > 0:
#             print('【已借阅的图书列表】')
#             for book in borrowed_books:
#                 print(f'编号：{book.book_id}，标题：{book.title}')
#         else:
#             print('未借阅图书')
# if __name__ == '__main__':
#     m1 = NormalMember('VIP1','fly','060712')
#     print(m1)

# dataclass 用来存放数据
#filed 用于对字段（属性）更具体的设置（对字段用函数定义）
# 控制打印时是否要显示用repr-->filed(repr=False)不显示
from dataclasses import dataclass,field
import random
@dataclass(order=True)
class person:
    name:str
    age:int = field(repr=False)
    # default_factory用来接收不需要参数的可调用函数
    height:int = field(default_factory=lambda: random.randint(150,200))
if __name__ == '__main__':
    p1 = person('fly',20)
    p2 = person('fqq',23)
    print(p1==p2)
    # 如果要比较大小，要将装饰器的order属性设为True
    print(p1 > p2)