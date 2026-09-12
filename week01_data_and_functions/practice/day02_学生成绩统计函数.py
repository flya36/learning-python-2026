'''
封装一个函数 `calc_score_stats(scores)`,接收一个整数列表(代表多名学生的成绩),返回统计结果:平均分、最高分、最低分、及格人数(≥60 分)。
额外要求：
- 增加一个可选参数 `pass_line`，默认值为 60,支持自定义及格线
- 如果传入空列表，返回 `None` 并在函数内打印提示，程序不报错
- 主程序调用该函数，传入 2~3 组不同的成绩列表，打印完整统计结果
'''
def calc_score_stats(scores: list[int],pass_line = 60):
    '''
    接收一个整数列表(代表多名学生的成绩),返回统计结果:平均分、最高分、最低分、及格人数(≥60 分)
    :param scores 学生成绩列表
    :param pass_line 默认及格线
    return: 平均分、最高分、最低分、及格人数
    '''
    if not scores:
        return None
    max_score = max(scores)
    min_score = min(scores)
    ave_score = round(sum(scores) / len(scores),1)
    pass_count = sum(1 for score in scores if score >= pass_line)
    return max_score,min_score,ave_score,pass_count 
stu_scores = []
while True:
    score = int(input('请输入学生成绩（输入-1视为结束):'))
    if score == -1:
        print('输入结束')
        break
    else:
        stu_scores.append(score)
result = calc_score_stats(stu_scores)
if result is not None:
    max_s, min_s, ave_s, pass_stu = result
    print(f'max:{max_s}, min:{min_s}, ave:{ave_s}, pass:{pass_stu}')
else:
    print("没有成绩数据，无法统计")