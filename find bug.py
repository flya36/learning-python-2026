total = 0
i = 1
# 目标：求1~10偶数之和，正确结果应该是 2+4+6+8+10 = 30
while i <= 10:
    if i % 2 == 0:
        total = total + i
    i = i + 1

print("偶数总和：", total)