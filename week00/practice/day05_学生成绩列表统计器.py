student_score = []
total_score =0
while True:
    score = int(input('请输入学生成绩（输入-1视为结束）'))
    if score == -1:
        break
    total_score += score
    student_score.append(score)
if len(student_score) == 0:
    print("未输入任何成绩")
else:
    average_score = total_score/len(student_score)
    student_score.sort()
    print(f'成绩由低到高排序为：{student_score}，最高分：{max(student_score)}，最低分：{min(student_score)}，平均分：{average_score:.1f}')