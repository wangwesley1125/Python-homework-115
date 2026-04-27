max=0
mini=0
sum=0
for i in range(0,10,1):
    n=input(print("輸入數字",i+1,":"))
    n1=int(n)
    print(n1)
    if(n1>max):
        max=n1
    if(n1<mini):
        mini=n1
    sum=sum+n1
avg=sum/10
print("最大值:",max,",最小值:",mini,",平均值:",avg)
