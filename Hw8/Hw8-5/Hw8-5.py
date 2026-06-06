'''
(Dictionary Manipulations) Using the following dictionary, which maps country
names to abbreviations:
tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
Write a script that shows the user a list of dictionary manipulation options to choose
from. Based on the choice, the corresponding manipulation is performed, and the result
is shown on the screen. The following choices can be made by the user:
a) Show the abbreviation of a country chosen by the user.
b) Display all key-value pairs in a two-column format.
c) Add a new key-value pair to the dictionary or change the value of an existing
key-value pair.
d) Create a new dictionary with the values of the first dictionary as keys and the
keys of the first dictionary as values.
e) Convert all the abbreviations in the dictionary to uppercase letters.
'''

def op_a():
    print("顯示國家/地區的縮寫")

def op_b():
    print("以兩列格式顯示所有鍵值對")

def op_c():
    print("在字典中新增新的鍵值對或變更現有鍵值對的值")

def op_d():
    print("建立一個新字典，以第一個字典的值作為鍵，以第一個字典的鍵作為值")

def op_e():
    print("將字典中的所有縮寫轉換為大寫字母")

tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

user = input("本字典的操作清單:\n" + 
             "a) 顯示國家/地區的縮寫\n" + 
             "b) 以兩列格式顯示所有鍵值對\n" + 
             "c) 在字典中新增新的鍵值對或變更現有鍵值對的值\n" + 
             "d) 建立一個新字典，以第一個字典的值作為鍵，以第一個字典的鍵作為值\n" + 
             "e) 將字典中的所有縮寫轉換為大寫字母\n" + 
             "請輸入選項:")

if user == "a":
    op_a()
elif user == "b":
    op_b()
elif user == "c":
    op_c()
elif user == "d":
    op_d()
elif user == "e":
    op_e()
else:
    print("無此選項，請重新選擇!")