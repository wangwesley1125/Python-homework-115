import statistics
n=[]
avg=0
summ=0

for i in range(1,11):
    n1=int(input(f'請輸入第{i}個整數:'))
    n.append(n1)

max=n[0]
min=n[0]

for j in range(0,10):
    summ+=n[j]
    if n[j]>max:
        max=n[j]
    elif n[j]<min:
        min=n[j]

avg=summ/len(n)
std_dev = statistics.stdev(n)

print(f'分數列{n}')
print(f'最大值:{max},最小值:{min},平均值:{avg},標準差{std_dev}')