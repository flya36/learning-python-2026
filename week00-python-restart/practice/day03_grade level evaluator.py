#学会使用try-except
try:
    grade = int(input('请输入成绩：'))
    if 0 <= grade < 60:
        print('D')
    elif 60 <= grade < 80:
        print('C')
    elif 80 <= grade < 90:
        print('B')
    elif 90 <= grade <= 100:
        print('A')
    else:
        print('成绩输入异常')
except ValueError:
    print('输入不是有效整数')