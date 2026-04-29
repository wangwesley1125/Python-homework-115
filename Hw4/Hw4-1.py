def average(*args):

    if len(args)==0:
        return 0
    
    total=sum(args)
    count=len(args)

    return total/count


print(f"平均值 1: {average(10, 20, 30)}")          # 3 個參數
print(f"平均值 2: {average(1, 2, 3, 4, 5, 6, 7)}") # 7 個參數
print(f"平均值 3: {average(100)}")                # 1 個參數
print(f"平均值 4: {average()}")                   # 0 個參數