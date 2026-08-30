'''
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称:xxx,商品价格:xxx,商品数量:xxx"。
5.退出购物车
'''

menu = '''
############# 购物车系统 #############
#           1.添加购物车             #
#           2.修改购物车             #
#           3.删除购物车             #
#           4.查询购物车             #
#           5.退出购物车             #
#####################################
'''

#{goods_ name:{goods_price:price,goods_num:num}}
shopping_cart = {}
print('欢迎使用购物车管理系统！')
while True:
    print(menu)
    choice = input('请输入操作:')
    match choice:
        # 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车
        case '1':
            goods_name = input('请输入商品名称：')
            if goods_name in shopping_cart:
                print('当前商品已在购物车里')
            else:
                price = float(input('请输入商品价格：'))
                num = int(input('请输入商品数量：'))
                shopping_cart[goods_name] = {'goods_price':price,'goods_num':num}
                print('已添加')

        # 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息
        case '2':
            goods_name = input('请输入商品名称：')
            if goods_name  not in shopping_cart:
                print('当前商品不存在')
            else:
                price = float(input('请输入商品价格：'))
                num = int(input('请输入商品数量：'))
                shopping_cart[goods_name] = {'goods_price':price,'goods_num':num}
                print('已修改')

        # 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品
        case '3':
            goods_name = input('请输入商品名称：')
            if goods_name in shopping_cart:
                del shopping_cart[goods_name]
                print('已删除')
            else:
                print('该商品不存在')

        # 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称:xxx,商品价格:xxx,商品数量:xxx"
        case '4':
            if len(shopping_cart) == 0:
                print('购物车无商品')
            else:
                for name in shopping_cart:
                    print(f"商品名称:{name},商品价格:{shopping_cart[name]['goods_price']},商品数量:{shopping_cart[name]['goods_num']}")

        # 退出购物车
        case '5':
            print('已退出')
            break
        case _:
            print('非法操作，请重新输入')