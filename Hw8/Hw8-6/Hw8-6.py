'''
(Set Manipulation) Write a script where two sets of colors are created. Write functions that use either the comparison operators or the mathematical set operators to display
the following results:
a) Display the set with the highest number of elements.
b) Display whether Set 1 = Set 2.
c) Display the results of the |, &, -, and ^ operations.
'''

color1 = {'red', 'green', 'blue'}
color2 = {'purple', 'red', 'pink', 'orange'}

print("===== 最多元素量的集合是 =====")

if len(color1) > len(color2):
    print("Color1 元素最多!\n")
else:
    print("Color2 元素最多!\n")

print("===== 是否 Color1 等於 Color2 =====")
if color1 == color2:
    print("Color1 和 Color2 相等!\n")
else:
    print("Color1 和 Color2 不相等!\n")

print("===== 集合運算如下 =====")
# 聯集
print(color1 | color2)

# 交集
print(color1 & color2)

# 差集
print(color1 - color2)

# 對稱差集
print(color1 ^ color2)