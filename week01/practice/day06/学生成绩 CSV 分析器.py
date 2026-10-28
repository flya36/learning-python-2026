# import csv
# from pathlib import Path
# import json
# # 编写函数 `calc_subject_avg(data)`，计算每门课程的平均分，返回字典
# def calc_subject_avg(data:list)-> dict :
#     subject_info = {}
#     for info in data:
#         subject = info['subject'] 
#         if subject not in subject_info:
#             subject_info[subject] = {"total_score": 0, "subject_count": 0}
#         subject_info[subject]['total_score'] += int(info['score'])
#         subject_info[subject]['subject_count'] += 1
#     subject_ave = {}
#     for subject in subject_info:
#         subject_ave[subject] = subject_info[subject]['total_score']/subject_info[subject]['subject_count']
#     return subject_ave
# def get_grade(score:float)->str:
#     if 100 >= score >= 90:
#         return 'A'
#     elif 90 > score >=80:
#         return 'B'
#     elif 80 > score >=60:
#         return 'C'
#     elif 60 > score >= 0:
#         return 'D'
#     else:
#         return '分数异常'

    
# csv_path = Path(__file__).parent/'scores.csv'
# # 读取 CSV 文件，将数据存储为字典列表
# with open(csv_path,'r',encoding='utf-8')as f:
#     reader = csv.DictReader(f)
#     data = []
#     failure_count = 0
#     for row in reader:
#         if '0' < row['score'] < '60':
#             failure_count += 1
#         data.append(row)
#     res = max(data,key= lambda x:x['score'])
#     max_score_name = res['name']
#     max_score_subject = res['subject']
# subject_ave = calc_subject_avg(data)
# score_analysis = {
#     'subject_ave':subject_ave,
#     'failure_count':failure_count,
#     'max_score_student':max_score_name,
#     'max_score_subject':max_score_subject
# }
# with open(Path(__file__).parent/'score_analysis.json','w',encoding='utf-8')as f:
#     json.dump(score_analysis,f,ensure_ascii=False,indent=2,sort_keys=True)

import csv
import json
from pathlib import Path


def read_scores(file_path: str|Path) -> list[dict]:
    # """读取CSV文件，转换为字典列表，分数转为整数"""
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"文件 {file_path} 不存在")

    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 核心修正：分数转为数值类型
            row["score"] = int(row["score"])
            data.append(row)
    return data


def calc_subject_avg(data: list[dict]) -> dict[str, float]:
    """计算每门课程的平均分，返回字典"""
    subject_info = {}
    for info in data:
        subject = info["subject"]
        if subject not in subject_info:
            subject_info[subject] = {"total_score": 0, "count": 0}
        subject_info[subject]["total_score"] += info["score"]
        subject_info[subject]["count"] += 1

    subject_avg = {}
    for subject, info in subject_info.items():
        subject_avg[subject] = round(info["total_score"] / info["count"], 2)
    return subject_avg


def get_grade(score: float) -> str:
    # """根据分数返回等级：≥90为A，≥80为B，≥60为C，<60为D"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


def analyze_scores(data: list[dict]) -> dict:
    """完整统计分析：平均分、不及格人数、最高分、等级"""
    # 1. 课程平均分
    subject_avg = calc_subject_avg(data)

    # 2. 不及格学生人数（去重）
    fail_students = {row["name"] for row in data if row["score"] < 60}
    fail_count = len(fail_students)

    # 3. 最高分记录（数值比较）
    max_score_row = max(data, key=lambda x: x["score"])
    max_score_info = {
        "name": max_score_row["name"],
        "subject": max_score_row["subject"],
        "score": max_score_row["score"],
        "grade": get_grade(max_score_row["score"])
    }

    # 4. 学生个人平均分（可选补充，符合综合题要求）
    student_scores:dict = {}
    for row in data:
        name = row["name"]
        if name not in student_scores:
            student_scores[name] = []
        student_scores[name].append(row["score"])
    student_avg = {
        name: round(sum(scores) / len(scores), 2)
        for name, scores in student_scores.items()
    }

    return {
        "subject_avg": subject_avg,
        "fail_student_count": fail_count,
        "max_score": max_score_info,
        "student_avg": student_avg
    }


def main():
    # 支持相对路径，不依赖 __file__
    csv_path = Path(__file__).parent/'scores.csv'
    output_path = Path(__file__).parent/"score_analysis.json"

    data = read_scores(csv_path)
    result = analyze_scores(data)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2, sort_keys=True)

    print("分析完成，结果已保存到", output_path)
    print("统计结果：", result)


if __name__ == "__main__":
    main()
