grade = {} # 字典格式 = {"學生姓名" : [score1, score2, score3]}

count_input_std_name_times = 0

# 要求使用者輸入四個學生的名字跟三次考試成績
while count_input_std_name_times < 4:
    student_name = input("學生姓名:")
    score1 = int(input("第一個成績:"))
    score2 = int(input("第二個成績:"))
    score3 = int(input("第三個成績:"))
    # print(f"學生姓名: {student_name}, 第一個成績: {score1}, 第二個成績: {score2}, 第三個成績: {score3}")
    grade[student_name] = [score1, score2, score3] # 放入字典
    count_input_std_name_times += 1

# print(count_input_std_name_times)

each_rank = 0

# 針對每次成績去排序
for j in range(3):
    rank = sorted(grade.items(), key=lambda x: x[1][j], reverse = True)
    # print(f"{rank}")
    print(f"第 {j + 1} 次考試成績:")
    for key, value in rank:
        print(f"{each_rank % 4 + 1} {key} {value[j]}")
        each_rank += 1
    print(end = "\n")