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

# 讓使用者可以查詢國家的縮寫
def op_a(dict):

    while True:
        print(end="\n")
        
        choose_country = input("====== 查詢國家縮寫 ======\n" + 
            "(1) Canada (2) United States (3) Mexico (q) 返回操作清單\n" +
            "請輸入選項>> ")
        
        if choose_country == "q":
            print(end="\n")
            main()

        country = ""

        if choose_country == "1":
            country = "Canada"
        elif choose_country == "2":
            country = "United States"
        elif choose_country == "3":
            country = "Mexico"

        for key, value in dict.items():
            if key == country:
                print(f"{key} 的縮寫是 {value}")

# 將字典的 key 和 value 分別對應出來
def op_b(dict_format):

    print(end="\n")

    print(f"{"國家": <10} 縮寫")

    for key, value in dict_format.items():
        print(f"{key: <12} -> {value}")

    print(end="\n")

    main()

# 可以新增新的 key, value 或改變字典現有的 value
def op_c(dict):
    
    print(end="\n")

    add_key_value = {}
    change_new_value = {}

    function = input("(1) 新增國家 (2) 變更國家的縮寫 >> ")

    # 顯示新增國家和新增國家縮寫到 add_key_value 字典
    if function == "1":
        new_country = input("請輸入國家名稱: ")
        new_abbreviation = input("請輸入新增國家的縮寫: ")
        
        add_key_value[new_country] = new_abbreviation

        # print(add_key_value)

        dict.update(add_key_value)

        print("====== 更新字典 ======")
        for key, value in dict.items():
            print(f"{key} {value}")

    elif function == "2":
        print("====== 目前字典內容 ======")
        for key, value in dict.items():
            print(f"{key} {value}")

        while True:
            change_dict_key = input("請輸入想變更縮寫的國家名稱: ")

            # 提醒使用者沒有此國家
            if change_dict_key not in dict:
                print("字典中無此國家，請重新輸入!")
            
            else:
                break

        change_dict_value = input("此國家的縮寫更改為: ")

        

        change_new_value[change_dict_key] = change_dict_value

        dict.update(change_new_value)

        print(end="\n")

        print("====== 修改後字典內容 ======")
        for key, value in dict.items():
            print(f"{key} {value}")


    print(end="\n")

    main()


# 將 key 和 value 對調
def op_d(dict):
    
    print(end="\n")

    new_tlds = {}

    # 放入新的字典裡
    for key, value in dict.items():
        new_tlds[value] = key

    # 顯示新的字典
    print("====== 新字典 ======")
    for new_key, new_value in new_tlds.items():
        print(f"{new_key} {new_value}")

    print(end="\n")
    main()

# 將縮寫都轉成大寫
def op_e(dict):
    print(end="\n")

    print(f"{"國家": <10} 縮寫")

    for key, value in dict.items():
        print(f"{key: <12} -> {value.upper()}")

    print(end="\n")

    main()

# 主程式
def main():
    user = input("====== 本字典的操作清單 ======\n" + 
                "(a) 顯示國家/地區的縮寫\n" + 
                "(b) 以兩列格式顯示所有鍵值對\n" + 
                "(c) 在字典中新增新的鍵值對或變更現有鍵值對的值\n" + 
                "(d) 建立一個新字典，以第一個字典的值作為鍵，以第一個字典的鍵作為值\n" + 
                "(e) 將字典中的所有縮寫轉換為大寫字母\n" + 
                "(q) 退出程式\n"
                "請輸入選項>> ")
    
    if user == "a":
        op_a(tlds)
    elif user == "b":
        op_b(tlds)
    elif user == "c":
        op_c(tlds)
    elif user == "d":
        op_d(tlds)
    elif user == "e":
        op_e(tlds)
    elif user == "q":
        exit()
    else:
        print("\n無此選項，請重新選擇!\n")
        main()
    print(end="\n")

# 字典
tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# 主程式
main()