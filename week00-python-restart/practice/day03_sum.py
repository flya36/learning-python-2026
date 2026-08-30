#while循环
sum = 0
i,j = 1,0
while i <101:
    sum += i
    if i % 2 == 0:
        j += 1
    i += 1
print(f'1-100的和为：{sum}')
print(f'1-100之间的偶数个数为：{j}')
#for循环
sum = 0
j = 0
for i in range(1,101):
    sum += i
    if i % 2 == 0:
        j += 1
print(f'1-100之间的和为：{sum}')
print(f'1-100之间的偶数个数为：{j}')