# 异常处理
try:
    print("============")
    # print(my_name)
    print(1/0)
    print('============')
except NameError as e:
    print('程序运行出错，',e)
# except ZeroDivisionError as e:
#     print('0不能作为被除数')
except Exception as e:
    print('程序出错，请联系工作人员：',e)
finally:
    print('资源释放')