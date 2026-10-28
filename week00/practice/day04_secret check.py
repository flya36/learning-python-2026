'''1. 设置正确密码字符串，例如`secret = "python123"`
2. 允许用户最多输入 3 次密码
3. 如果输入正确：打印 “密码正确，通过！”，结束程序
4. 如果输错，提示还剩余几次机会
5. 3 次全部错误，打印 “尝试次数耗尽，拒绝访问”，结束。'''
secret = 'fly123'
chance = 3
while True:
    password = input('请输入您的密码：')
    chance -= 1
    if password == secret:
        print('密码正确，通过！')
        break
    elif chance > 0:
        print(f'密码输入错误，当前剩余机会{chance}')
    else:
        print('尝试次数耗尽，拒绝访问')
        break