i=1
while i<=9:
    j=1
    while j<=9:
        S=f"{i}x{j}={i*j}"
        print(f"{S:<10}",end="")
        j+=1
    i+=1
    print()