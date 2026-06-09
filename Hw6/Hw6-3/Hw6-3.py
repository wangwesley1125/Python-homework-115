'''
Given the two-by-three integer list t
    t = [[10, 7, 3], [20, 4, 17]]

a) Determine and display the average of t’s elements using nested for statements to
iterate through the elements.

b) Write a for statement that determines and displays the average of t’s elements 
using the reductions sum and len to calculate the sum of each row’s elements and the number of elements in each row.
'''

t = [[10, 7, 3], [20, 4, 17]]

total = 0 # 數字的總和
items = 0 # 數字的個數

for row in t:
    # print(row)
    for item in row:
        total += item
        # print(total)
        items += 1
        # print(items)

print("a)")
print(f"Total: {total}")
print(f"Items: {items}")
print(f"Average: {total / items}")

print("=================================")

total = 0 # 數字的總和
items = 0 # 數字的個數

for row in t:
    total += sum(row)
    items += len(row)

print("b)")
print(f"Total: {total}")
print(f"Items: {items}")
print(f"Average: {total / items}")