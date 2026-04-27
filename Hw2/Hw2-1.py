print('(a)')
for i in range(1,11):
    for j in range(i):
        print('*',end='')
    print()

print('(b)')
for i in range(1,11):
    for j in range(11-i):
        print('*',end='')
    print()

print('(c)')
for i in range(1,11):
    for j in range(i):
        print(' ',end='')
    for k in range(11-i):
        print('*',end='')
    print()

print('(d)')
for i in range(1,11):
    for j in range(11-i):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    print()