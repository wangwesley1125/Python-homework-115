list1 = ['a', 'b', 'c', 'd', 'e', 'f']

a = list1[1:3]
print(a)

b = list1[-4:-2]
print(b)

c = list1[:4]
print(c)

d = list1[4:]
print(d)

e = list1[2:len(list1)]
print(e)

f = list1[1:3][1]
print(f)

g = list1[3:2]
print(g)

del list1[1:3]
print(list1)

print("=================================")

a = list("abcdefg")

print(a)

print(a[1:3])

a[1:3] = [1, 2]
print(a)

print(a[1:2])

a[1:2] = [5, 6, 7]
print(a)

print(a[2:5])

a[2:5] = []
print(a)

print(a[2:2])

a[2:2] = [7, 8, 9]
print(a)