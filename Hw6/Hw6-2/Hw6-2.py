a = [x for x in range(5)]
print(a)

b = [i for i in range(0, 10, 3)]
print(b)

c = [k for k in range(0, 10) if k % 2 == 0]
print(c)

d = [x for x in "sakura"]
print(d)

e = [x**3 for x in range(5)]
print(e)

f = [x.upper() for x in "sakura"]
print(f)

g = [x*2 for x in ["haha", "hihi", "hehe"]]
print(g)

h = [(x, y) for x in range(3) for y in range(4)]
print(h)

k = [(x, y) for x in range(3) for y in range(4) if x != y]
print(k)

l = [(x, x**0.5) for x in range(5)]
print(l)