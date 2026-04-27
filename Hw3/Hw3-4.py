import random

def play_game():

    keep_playing = True
    
    while keep_playing:
        a=random.randint(1, 10)
        b=random.randint(1, 10)
        c=a*b
        d=int(input(f"請輸入{a}X{b}="))

        if d==c:
            print("你答對了")
            choice = input("要繼續玩嗎？(y/n): ").lower()
            if choice != 'y':
                print("使用者已結束遊戲")
                keep_playing = False
        else:
            # 5. 答錯則強制結束遊戲
            print(f"答錯了,正確答案是 {c}。")
            print("遊戲結束")
            keep_playing = False

if __name__ == "__main__":
    play_game()