# #输入一个正整数 n，打印从 n 往下数到 1，遇到数字 7 直接跳过不打印

#这一版太复杂了
# n = int(input('请输入一个正整数：'))
# while n > 0:
#     if n == 7:
#         n -= 1
#         continue
#     print(n)
#     n -= 1

#精进的一版
# n = int(input('请输入一个正整数：'))
# while n > 0:
#     if n != 7:
#         print(n)
#     n -= 1   


# #for 版本
# n = int(input('请输入整数：'))
# for i in range(n,0,-1):
#     if i == 7:
#         continue
#     print(i)