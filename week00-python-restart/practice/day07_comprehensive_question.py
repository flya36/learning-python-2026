'''
学生成绩综合统计
输入一个学生成绩列表，每个元素是字典格式：{"姓名":"xxx", "科目":"xxx", "分数": 数字}。
编写函数 analyze_scores(score_list)，返回一个字典，包含以下 3 个结果：
1. 'all_subjects'：所有不重复的科目（用列表输出）
2. 'subject_avg'：每个科目的平均分（保留 1 位小数）
3. 'failed_students'：所有不及格（<60 分）的学生姓名（去重，用列表输出）
'''
# def analyze_scores(score_list):
    # result = {}
    # result["all_subjects"] = list(set(student["科目"] for student in score_list))
    # result["failed_students"] = list(set([student["姓名"] for student in score_list if student["分数"] < 60]))
    # subject_score = {}
    # subject_count = {}
    # subject_avg = {}
    # for student in score_list:
    #     if student["科目"] not in subject_score:
    #         subject_score[student["科目"]] = student["分数"]
    #     else:
    #         subject_score[student["科目"]] += student["分数"]
    #     if student["科目"] not in subject_count:
    #         subject_count[student["科目"]] = 1
    #     else:
    #         subject_count[student["科目"]] += 1
    # for subject in subject_score:
    #     subject_avg[subject] = round(subject_score[subject]/subject_count[subject],1)
    # result['subject_avg'] = subject_avg
    # return result
    #前面写的太冗余，简化版
def analyze_scores(score_list):
    subject_total = {}
    subject_count = {}
    failed_set = set()

    for stu in score_list:
        sub = stu["科目"]
        score = stu["分数"]

        # 同步累加总分和人数
        if sub in subject_total:
            subject_total[sub] += score
            subject_count[sub] += 1
        else:
            subject_total[sub] = score
            subject_count[sub] = 1

        # 不及格直接加入集合（自动去重）
        if score < 60:
            failed_set.add(stu["姓名"])

    # 字典推导式计算平均分
    subject_avg = {sub: round(total / subject_count[sub], 1) for sub, total in subject_total.items()}

    return {
        "all_subjects": list(subject_total.keys()),
        "subject_avg": subject_avg,
        "failed_students": list(failed_set)
    }


students_scores = []
while True:
    student_score = {}
    name = input('请输入学生姓名(输入-1视为结束):')
    if name == '-1':
        print('输入完成')
        break
    else:
        subject = input('请输入学生科目：')
        score = int(input('请输入学生分数：'))
        student_score["姓名"] = name
        student_score["科目"] = subject
        student_score["分数"] = score
        students_scores.append(student_score)
print(analyze_scores(students_scores))



'''
## 访问日志异常分析
输入日志字典列表，每条日志格式：`{"ip":"xxx", "访问路径":"xxx", "状态码": 数字}`。
编写函数 `analyze_logs(log_list)`，返回字典，包含：
1. `ip_count`：每个 IP 的访问次数
2. `error_ips`：出现过 4xx/5xx 错误状态码的 IP(去重列表)
3. `unique_paths`：所有不重复的访问路径列表
'''
def analyze_logs(log_list):
    result = {}
    error_ips = set()
    unique_paths = set()
    # `ip_count`：每个 IP 的访问次数
    ip_count = {}
    for log in log_list:
        # =ip_count.get(ip, 0) + 1（95-98行）
        if log['ip'] not in ip_count:
            ip_count[log['ip']] = 1
        else:
            ip_count[log['ip']] += 1
    # `error_ips`：出现过 4xx/5xx 错误状态码的 IP(去重列表)
    # error_ips = list(set([log['ip'] for log in log_list if log['状态码'] // 100 == 4 or log['状态码'] // 100 == 5]))
    #多了一次遍历，实际项目效率差
        if log['状态码'] // 100 == 4 or log['状态码'] // 100 == 5:
            error_ips.add(log['ip'])
    # `unique_paths`：所有不重复的访问路径列表
    # unique_paths = list(set(log['访问路径'] for log in log_list))
    # 也是一样多一次遍历效率就越差
        unique_paths.add(log['访问路径'])
    result['ip_count'] = ip_count
    result['error_ips'] = list(error_ips)
    result['unique_paths'] = list(unique_paths)
    return result

dialog_list = []
while True:
    log_dict = {}
    ip = input('请输入ip(输入-1视为结束):')
    if ip == '-1':
        break
    else:
        route = input('请输入访问路径：')
        code = int(input('请输入状态码'))
        log_dict['ip'] = ip
        log_dict['访问路径'] = route
        log_dict['状态码'] = code
    dialog_list.append(log_dict)
print(analyze_logs(dialog_list))