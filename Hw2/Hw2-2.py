number=1537
d=2

r=number
f=[]

while d*d<=r:
    if r%d==0:
        f.append(d)
        r//=d
    else:
        d+=1

if r>1:
    f.append(r)

result = "*".join(map(str,f))

print(f"{number}={result}")