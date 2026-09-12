# # 函数定义
# def out_line():
#     print('----------')
# # 调用函数
# out_line()

# # 函数的参数和返回值
# def circle_area(r):     #r是形参，局部变量
#     area = 3.14*r**2
#     return area
# print(circle_area(10))     #10是实参

# # 计算圆的面积和周长，多个返回值用逗号分隔，会分配到元组中
# def circle_area_len(r):
#     '''
#     该函数是根据圆的半径计算出圆的面积和周长
#     :param r:半径
#     :return: 面积，周长
#     '''
#     return 3.14*r**2,round(2*3.14*r,1)
# help(circle_area_len)
# print(circle_area_len(10)) 

# # 函数的嵌套调用
# def function_a():
#     print('a...before')
#     function_b()
#     print('a...after')
# def function_b():
#     print('b...before')
#     function_c()
#     print('b...after')
# def function_c():
#     print('c...over')
# function_a()

# # 1．定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。
# def triangel_area(b,h):
#     '''
#     根据传入的底和高计算三角形面积的函数
#     :param b:三角形的底
#     :param h:三角形的高
#     :return:三角形的面积
#     '''
#     return b * h / 2
# print(triangel_area(10,8))

# # 2．定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
# def count_aeiou(s):
#     '''
#     计算传入的字符串中元音字母的个数
#     :param s:传入的字符串
#     :return:元音个数
#     '''
#     count = 0
#     for i in s:
#         if i in 'aeiouAEIOU':
#             count += 1
#     return count
# print(count_aeiou('hello world'))

# # 3．定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分 (保留 1 位小数)，并返回。
# def cal_scores(score_list):
#     max_score = max(score_list)
#     min_score = min(score_list)
#     ave_score = round(sum(score_list)/len(score_list),1)
#     return max_score,min_score,ave_score
# scores = [328,483,741,642,356,245]
# max_score,min_score,ave_score = cal_scores(scores)
# print(f'最高分:{max_score},最低分:{min_score},平均分:{ave_score}')

# '''
# 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# - 分数 >= 90: A
# - 分数 >= 75: B
# - 分数 >= 60: C
# - 分数 < 60: D
# '''
# def grade_level(scores):
#     grade_dict = {}
#     for score in scores:
#         if score >= 90:
#             grade_dict[score] = 'A'
#         elif score >= 75:
#             grade_dict[score] = 'B'
#         elif score >= 60:
#             grade_dict[score] = 'C'
#         elif score < 60:
#             grade_dict[score] = 'D'
#     return grade_dict
# scores_list = []
# while True:
#     score = int(input('请输入成绩（输入-1视为结束）：'))
#     if score == -1:
#         print('输入完毕')
#         break
#     scores_list.append(score)
# print(grade_level(scores_list))


# '''
# 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒
# '''
# def time_conversion(sec):
#     h = sec // 3600
#     m = sec % 3600 //60
#     s = sec - h*3600 - m*60
#     time = {'hour':h,'minute':m,'second':s}
#     return time
# sec = int(input('请输入秒：'))
# print(time_conversion(sec))

# # 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）
# def triangle_type(a,b,c):
#     if a+b > c and a+c > b and b+c > a:
#         if a == b and b == c:
#             print('等边三角形')
#         elif a == b or b == c or a == c:
#             print('等腰三角形')
#         else:
#             print('普通三角形')
#     else:
#         print('不构成三角形')
# triangle_type(1,2,3)

# # 位置参数
# def stu(name,age,gender):
#     print(f'姓名：{name},年龄：{age}，性别：{gender}')
# stu('fly','女','20')
# # 关键字参数
# stu(age='23',name='fqq',gender='女')
# # 混合使用-->位置参数必须在关键字参数之前
# stu('wxh',gender='女',age='51')


# # 默认参数-->默认参数必须在没有默认参数的形参之后，若没改变则为默认参数，若改变则可改变
# def stu(name,age,gender='女'):
#     print(f'姓名：{name},年龄：{age}，性别：{gender}')
# stu('张三','21')
# stu('张三','21','男')

# # 递归调用（函数中自己调用自己）-->计算阶乘
# def jc(num):
#     if num == 1 or num == 0:
#         return 1
#     else:
#         return num * jc(num - 1)
# print(jc(10))
# print(jc(0))

# # 不定长参数 默认参数
# '''
# 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
# 具体规则如下：
# - 优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
# - 积分抵扣需要商品总金额满 5000 才可以使用，100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
# '''
def calc_order_cost(*goods_info:tuple[str,float,int],coupon=0,cost=0,express=0.0):
    '''
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param *goods_info 商品信息（商品名、价格、数量）
    :param coupon 优惠券
    :param cost 积分抵扣
    :param express 运费信息
    :return:订单的总金额
    '''
    total_goods = [goods[1] * goods[2] for goods in goods_info]
    total_cost = sum(total_goods) + express
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    if total_cost >= 5000 and cost // 100 <= total_cost:
        total_cost -= cost // 100
    return total_cost
total = calc_order_cost(('cellphon',5999,5),('elc toothbrush',200,5),coupon=5000,cost=9800)
print(f'金额总价：{total}')

# # 类型注解-->变量：数据类型
# name: list[str] =[]
# name.append('a')
# name.append(1)
