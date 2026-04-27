print('(while)')

i=1
while i<=9:
    j=1
    while j<=i:
        print(j,end='')
        j+=2
    i+=2
    print()


print('(for)')

for i in range(1,10,2):
    for j in range(1,i+1,2):
        print(j,end='')
    print()