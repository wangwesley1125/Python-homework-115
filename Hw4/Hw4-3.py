list1=[]
for i in range(1,11):
    print(f'第{i}位學生')
    name=input('姓名:')
    score=int(input('分數:'))
    item=[name,score]
    list1+=[item]

print(list1)