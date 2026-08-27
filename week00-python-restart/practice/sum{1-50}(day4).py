# 求 1 ~ 50 之间所有 3 的倍数的总和
sum = 0
for i in range(1,51):
    if i % 3 ==0:
        sum += i
    i += 1
print(f'1 ~ 50 之间所有 3 的倍数的总和为：{sum}')