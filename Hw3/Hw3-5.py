import random
def rps_game():
    # 初始化勝場計數器
    player_wins = 0
    computer_wins = 0
    round_count = 1
    
    choices = {0: "剪刀", 1: "石頭", 2: "布"}
    
    print("遊戲開始")

    while player_wins < 5 and computer_wins < 5:
        print(f"\n【第 {round_count} 回合】")
        print(f"目前戰績 - 玩家: {player_wins} | 電腦: {computer_wins}")
        
        user_input = input("請出拳 (0:剪刀, 1:石頭, 2:布, 或 q 退出): ").lower()
        
        if user_input == 'q':
            print("玩家中途離場。")
            break
            
        if user_input not in ['0', '1', '2']:
            print("無效輸入，請重新選擇！")
            continue
            
        player_choice = int(user_input)
        
        computer_choice = random.randrange(3) # 產生 0, 1, 2
        
        print(f"玩家出：{choices[player_choice]}")
        print(f"電腦出：{choices[computer_choice]}")
        
        # 3. 判斷勝負邏輯
        if player_choice == computer_choice:
            print("結果：平手！")
        elif (player_choice == 0 and computer_choice == 2) or \
             (player_choice == 1 and computer_choice == 0) or \
             (player_choice == 2 and computer_choice == 1):
            print("結果：玩家獲勝！")
            player_wins += 1
        else:
            print("結果：電腦獲勝！")
            computer_wins += 1
            
        round_count += 1

    # 4. 宣告最終冠軍
    print("\n==========================")
    if player_wins == 5:
        print("恭喜！你贏得了最終勝利！")
    elif computer_wins == 5:
        print("遺憾！電腦贏得了最終勝利。")
    print(f"最終戰績 - 玩家: {player_wins} | 電腦: {computer_wins}")
    print("==========================")

if __name__ == "__main__":
    rps_game()