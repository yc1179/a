import random

def generate_target_number(x1, x2):
    """生成目標數字"""
    return random.randint(x1, x2)

def play_game(x1, x2, max_guesses):
    """遊戲主程式"""
    target_number = generate_target_number(x1, x2)
    print(f"遊戲開始！目標數字在 {x1} 和 {x2} 之間。")

    guesses = 0
    while guesses < max_guesses:
        guess = int(input("請猜測一個數字："))
        guesses += 1

        if guess < target_number:
            print("猜的太低了！")
        elif guess > target_number:
            print("猜的太高了！")
        else:
            print(f"恭喜你猜對了！目標數字是 {target_number}！")
            break
    else:
        print(f"很可惜，你已經猜了{n}次了，遊戲結束！目標數字是 {target_number}。")

if __name__ == "__main__":
    x1 = 1  # 隨機數範圍的下限
    x2 = 100  # 隨機數範圍的上限
    max_guesses = 5  # 最大猜測次數
    play_game(x1, x2, max_guesses)