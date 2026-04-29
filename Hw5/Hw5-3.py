pascal = [[1]]

print("第 1 層: [1]")


for i in range(1, 10):
    prev_row = pascal[i-1]  
    current_row = [1]       
    
    for j in range(len(prev_row) - 1):
        new_value = prev_row[j] + prev_row[j+1]
        current_row.append(new_value)
    
    current_row.append(1)   
    pascal.append(current_row) 
    
    print(f"第 {i+1} 層: {current_row}")