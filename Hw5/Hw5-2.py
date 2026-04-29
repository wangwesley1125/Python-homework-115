import math
import statistics

scores = []
num_students = 3
num_exams = 4

for i in range(num_students):
    print(f'--第{i+1}位學生--')
    students_scores=[]
    for j in range(num_exams):
        s=int(input(f'第{j+1}次考試成績:'))
        students_scores.append(s)
    scores.append(students_scores)

def count(d):
    average=sum(d)/len(d)
    mx=max(d)
    mi=min(d)
    dev = statistics.stdev(d)
    return average,mx,mi,dev

print('--依學生--')
for i in range(num_students):
    avg,mx,mi,dev=count(scores[i])
    print(f'第{i+1}位:平均:{avg:.2f},最大{mx},最小{mi},標準差{dev:.2f}')

print('--依考試--')
for j in range(num_exams):
    avg,mx,mi,dev=count([scores[i][j]for i in range(num_students)])
    print(f'第{j+1}次:平均:{avg:.2f},最大{mx},最小{mi},標準差{dev:.2f}')