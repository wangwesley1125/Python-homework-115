n=int(input("請輸入一個二進制數字(僅包含 0 與 1):"))
d=0
p=1
r=n

while r>0:
    di=r%10
    d+=di*p
    r=r//10
    p*=2


print(f"二進位數字 {n} 的十進位等值為: {d}")
