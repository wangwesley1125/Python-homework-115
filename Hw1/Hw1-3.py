o=10
pu=0.03
pd=-0.03
print("Year\tMoney Per Hours\tUp&Down")
for n in range(1,6,1):
    w=o*(1+pu)**n
    w1=f"{w:.3f}"
    print(n,"\t",w1,"\tUp")
for n in range(1,3,1):
    w=o*(1+pd)**n
    w1=f"{w:.3f}"
    print(n,"\t",w1,"\t\tDown")