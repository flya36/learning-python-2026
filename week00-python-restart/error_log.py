# max/min/sort/sorted
max('变量名',key=lambda x:x['要比较的变量索引位置或键'])    #其它同理
# 表达式中保留几位小数
# round(表达式，保留小数的位数)，如下
round(subject_score[subject]/subject_count[subject],1)
# 要计算{"姓名":"xxx", "科目":"xxx", "分数": 数字}中每个科目的平均分
# 通过遍历字典将各科目总分和各科目出现次数分到两个字典，查询相同科目名称得到总分和次数以此计算平均数
# subject_score（各科目总分）subject_count（各科目出现次数）
for subject in subject_score:
    subject_avg[subject] = round(subject_score[subject]/subject_count[subject],1)
# 要善于使用各数据容器的方法（增删查改）
# 遍历要尽可能地减少，防止效率变低