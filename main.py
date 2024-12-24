
import random
import time

# タイピング用の単語リスト
words = [
    "python", "programming", "keyboard", "computer", "algorithm",
    "developer", "typing", "practice", "software", "coding"
]

def get_random_word():
    return random.choice(words)

def typing_game():
    score = 0
    print("タイピングゲームを開始します！")
    print("'q'を入力すると終了します。\n")
    
    while True:
        target_word = get_random_word()
        print(f"この単語をタイプしてください: {target_word}")
        start_time = time.time()
        
        user_input = input("> ")
        
        if user_input.lower() == 'q':
            break
            
        if user_input == target_word:
            elapsed_time = time.time() - start_time
            words_per_minute = (len(target_word) / 5) / (elapsed_time / 60)
            score += 1
            print(f"正解！ タイピング速度: {words_per_minute:.1f} WPM")
        else:
            print("不正解！ もう一度試してください。")
        
        print(f"現在のスコア: {score}\n")
    
    print(f"\nゲーム終了！ 最終スコア: {score}")

if __name__ == "__main__":
    typing_game()
