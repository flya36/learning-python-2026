'''
基于现有知识开发一个教务管理系统
开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5. 列出所有学生：遍历所有学生信息并输出。
6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
7. 退出系统。


'''
menu = '''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    1. 添加学生信息 2. 修改学生信息 3. 删除学生信息 4. 查询学生信息 5. 列出所有学生 6. 统计班级成绩  7. 退出系统          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
'''
# {student_name:{'chinese_score':chinese_score,'math_score':math_score,'english_scoore':english_score}}
students_info = {}
print('欢迎进入教务管理系统~')
while True:
    print(menu)
    choice = input('请输入操作：')
    match choice:
        # 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中
        # {student_name:{'chinese_score':chinese,'math':math_score,'english':english_score}}
        case '1':
            student_name = input('请输入学生姓名：')
            if student_name in students_info:
                print('该学生信息已添加')
            else:
                chinese_score = float(input('请输入学生语文成绩：'))
                math_score = float(input('请输入学生数学成绩：'))
                english_score = float(input('请输入学生英语成绩：'))
                students_info[student_name] = {'chinese':chinese_score,'math':math_score,'english':english_score}
                print('录入完成')
        # 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息
        case '2':
            student_name = input('请输入学生姓名：')
            if student_name not in students_info:
                print('该学生信息不存在')
            else:
                chinese_score = float(input('请输入学生语文成绩：'))
                math_score = float(input('请输入学生数学成绩：'))
                english_score = float(input('请输入学生英语成绩：'))
                students_info[student_name] = {'chinese':chinese_score,'math':math_score,'english':english_score}
                print('修改完成')
        # 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息
        case '3':
            student_name = input('请输入学生姓名：')
            if student_name not in students_info:
                print('该学生信息不存在')
            else:
                del students_info[student_name]
                print('删除完成')
        # 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出
        case '4':
            student_name = input('请输入学生姓名：')
            if student_name not in students_info:
                print('该学生信息不存在')
            else:
                print(f'姓名：{student_name},语文成绩：{students_info[student_name]['chinese']},数学成绩：{students_info[student_name]['math']},英语成绩：{students_info[student_name]['english']}')
        # 列出所有学生：遍历所有学生信息并输出
        case '5':
            if len(students_info) == 0:
                print('当前无学生')
            else:
                for student_name in students_info:
                    print(f'姓名：{student_name},语文成绩：{students_info[student_name]['chinese']},数学成绩：{students_info[student_name]['math']},英语成绩：{students_info[student_name]['english']}')
        # 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名
        case '6':
            # ch_list = []
            # m_list = []
            # en_list = []
            # for student_name in students_info:
            #     ch_list.append(students_info[student_name]['chinese'])
            #     m_list.append(students_info[student_name]['math'])
            #     en_list.append(students_info[student_name]['english'])
            # ch_list.sort()
            # m_list.sort()
            # en_list.sort()
            # print(f'语文最高分：{ch_list[-1]}，姓名：；最低分：{ch_list[0]}，姓名：；平均分：{sum(ch_list)/len(ch_list):.1f}')
            # print(f'数学最高分：{m_list[-1]}，姓名：；最低分：{m_list[0]}，姓名：；平均分：{sum(m_list)/len(m_list):.1f}')
            # print(f'英语最高分：{en_list[-1]}，姓名：；最低分：{en_list[0]}，姓名：；平均分：{sum(en_list)/len(en_list):.1f}')

            # students_info_list = []
            # for student_name in students_info:
            #     students_info_list.append((student_name,students_info[student_name]['chinese'],students_info[student_name]['math'],students_info[student_name]['english']))
            # chinese_max = sorted(students_info_list,(key=lambda x : x[1]))
            # math_max = sorted(students_info_list,(key=lambda x : x[2]))
            # english_max = sorted(students_info_list,(key=lambda x : x[3]))
            # print(f'语文最高分：{chinese_max[-1][1]}，姓名：{chinese_max[-1][0]}；最低分：{chinese_max[0][1]}，姓名：{chinese_max[0][0]}；平均分：{sum(x[1] for x in chinese_sorted)/len(chinese_max):.1f}')
            # print(f'数学最高分：{math_max[-1][2]}，姓名{math_max[-1][0]}；最低分：{math_max[0][2]}，姓名：{math_max[0][0]}；平均分：{sum(x[2] for x in chinese_sorted)/len(math_max):.1f}')
            # print(f'英语最高分：{english_max[-1][3]}，姓名：{english_max[-1][0]}；最低分：{english_max[0][3]}，姓名：{english_max[0][0]}；平均分：{sum(x[3] for x in chinese_sorted)/len(english_max):.1f}')

            chinese_max_name = max(students_info,key= lambda name:students_info[name]['chinese'])
            chinese_max = students_info[chinese_max_name]['chinese']
            ch_ave = sum(students_info[name]['chinese'] for name in students_info)/len(students_info)
            math_max_name = max(students_info,key= lambda name:students_info[name]['math'])
            math_max = students_info[math_max_name]['math']
            m_ave = sum(students_info[name]['math'] for name in students_info)/len(students_info)
            english_max_name = max(students_info,key= lambda name:students_info[name]['english'])
            english_max = students_info[english_max_name]['english']
            en_ave = sum(students_info[name]['english'] for name in students_info)/len(students_info)
            chinese_min_name = min(students_info,key= lambda name:students_info[name]['chinese'])
            chinese_min = students_info[chinese_min_name]['chinese']
            math_min_name = min(students_info,key= lambda name:students_info[name]['math'])
            math_min = students_info[math_min_name]['math']
            english_min_name = min(students_info,key= lambda name:students_info[name]['english'])
            english_min = students_info[english_min_name]['english']
            print(f"语文最高分：{chinese_max}，姓名：{chinese_max_name}；最低分：{chinese_min}，姓名：{chinese_min_name}；平均分：{ch_ave:.1f}")
            print(f"数学最高分：{math_max}，姓名：{math_max_name}；最低分：{math_min}，姓名：{math_min_name}；平均分：{m_ave:.1f}")
            print(f"英语最高分：{english_max}，姓名：{english_max_name}；最低分：{english_min}，姓名：{english_min_name}；平均分：{en_ave:.1f}")

        # 退出
        case '7':
            print('感谢使用，已退出')
            break
        # 输入错误
        case _:
            print('输入非法，请重新输入')



# 前一个解答不知道该如何找到最高分最低分对应学生姓名，通过问豆包得知使用max(),min()函数即可获得，参照如下
# eg: chinese_max_name = max(student_info key=lambda name:student_info[name]['chines'])
chinese_max_name = max(students_info, key=lambda name: students_info[name]['chinese'])
chinese_max = students_info[chinese_max_name]['chinese']
chinese_min_name = min(students_info, key=lambda name: students_info[name]['chinese'])
chinese_min = students_info[chinese_min_name]['chinese']
chinese_avg = sum(s['chinese'] for s in students_info.values()) / len(students_info)




# 还有一种解法，参照如下
# 初始化：先拿第一个学生当初始值
first_name = list(students_info.keys())[0]
chinese_max_score = students_info[first_name]['chinese']
chinese_max_name = first_name

# 逐个对比
for name in students_info:
    current_score = students_info[name]['chinese']
    if current_score > chinese_max_score:
        chinese_max_score = current_score
        chinese_max_name = name

print(f"语文最高分：{chinese_max_score}，姓名：{chinese_max_name}")
