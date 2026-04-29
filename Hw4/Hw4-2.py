import random

def gq ():
    a=random.randint(1, 9)
    b=random.randint(1, 9)

    return a,b

def game ():
    print('乘法遊戲，輸入(quit)結束')

    while True:
        n1,n2=gq()
        ans=n1*n2
        try:
            uin=input(f'請問{n1}x{n2}=?')
            if uin=='quit':
                print('使用者已手動關閉遊戲')
                break

            if int(uin)==ans:
                print('回答正確')
            else:
                print(f'答錯了，正確答案是:{n1}x{n2}={ans}')
        except ValueError:
            print('請輸入(quit)離開系統')

if __name__=="__main__":
    game()