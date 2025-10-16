import random
import time

def number_guessing_game():
    """
    数当てゲーム
    1-100の範囲でランダムな数字を当てるゲーム
    """
    print("\n" + "="*40)
    print("🎯 数当てゲーム")
    print("="*40)
    print("1から100までの数字を当ててください！")
    print("ヒント: 大きい/小さい で教えます。")
    
    # ランダムな数字を生成
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts
        
        try:
            # ユーザーからの入力
            guess = int(input(f"\n{attempts}回目: 数字を入力してください (残り{remaining}回): "))
            
            # 入力値のチェック
            if guess < 1 or guess > 100:
                print("❌ 1から100の範囲で入力してください。")
                continue
            
            # 結果の判定
            if guess == target:
                print(f"\n🎉 正解です！{attempts}回で当てました！")
                return
            elif guess < target:
                print("📈 もっと大きい数字です！")
            else:
                print("📉 もっと小さい数字です！")
                
        except ValueError:
            print("❌ 正しい数字を入力してください。")
    
    print(f"\n💔 ゲームオーバー！正解は {target} でした。")

def rock_paper_scissors():
    """
    じゃんけんゲーム
    コンピュータとじゃんけんをするゲーム
    """
    print("\n" + "="*40)
    print("✂️ じゃんけんゲーム")
    print("="*40)
    print("1: グー, 2: チョキ, 3: パー")
    
    choices = {1: "グー", 2: "チョキ", 3: "パー"}
    player_score = 0
    computer_score = 0
    
    while True:
        try:
            # プレイヤーの選択
            player_choice = int(input("\nあなたの選択 (1-3, 0で終了): "))
            
            if player_choice == 0:
                break
            elif player_choice not in [1, 2, 3]:
                print("❌ 1-3の数字を入力してください。")
                continue
            
            # コンピュータの選択
            computer_choice = random.randint(1, 3)
            
            print(f"\nあなた: {choices[player_choice]}")
            print(f"コンピュータ: {choices[computer_choice]}")
            
            # 勝敗判定
            if player_choice == computer_choice:
                print("🤝 あいこです！")
            elif ((player_choice == 1 and computer_choice == 2) or
                  (player_choice == 2 and computer_choice == 3) or
                  (player_choice == 3 and computer_choice == 1)):
                print("🎉 あなたの勝ち！")
                player_score += 1
            else:
                print("💻 コンピュータの勝ち！")
                computer_score += 1
            
            print(f"スコア - あなた: {player_score}, コンピュータ: {computer_score}")
            
        except ValueError:
            print("❌ 正しい数字を入力してください。")
    
    print(f"\n最終スコア - あなた: {player_score}, コンピュータ: {computer_score}")
    if player_score > computer_score:
        print("🏆 あなたの勝利です！")
    elif computer_score > player_score:
        print("💻 コンピュータの勝利です！")
    else:
        print("🤝 引き分けです！")

def simple_quiz():
    """
    簡単なクイズゲーム
    一般的な知識問題に答えるゲーム
    """
    print("\n" + "="*40)
    print("🧠 簡単クイズゲーム")
    print("="*40)
    print("3つの選択肢から正解を選んでください！")
    
    # クイズの問題と選択肢
    quizzes = [
        {
            "question": "日本の首都は？",
            "choices": ["1: 大阪", "2: 東京", "3: 京都"],
            "correct": 2
        },
        {
            "question": "1+1は？",
            "choices": ["1: 1", "2: 2", "3: 3"],
            "correct": 2
        },
        {
            "question": "空の色は？",
            "choices": ["1: 赤", "2: 青", "3: 緑"],
            "correct": 2
        },
        {
            "question": "リンゴは何色？",
            "choices": ["1: 赤", "2: 青", "3: 黄色"],
            "correct": 1
        },
        {
            "question": "太陽は何色？",
            "choices": ["1: 青", "2: 緑", "3: 黄色"],
            "correct": 3
        }
    ]
    
    score = 0
    total_questions = len(quizzes)
    
    # 問題をシャッフル
    random.shuffle(quizzes)
    
    for i, quiz in enumerate(quizzes, 1):
        print(f"\n--- 問題 {i} ---")
        print(quiz["question"])
        for choice in quiz["choices"]:
            print(choice)
        
        try:
            answer = int(input("答えを入力してください (1-3): "))
            
            if answer == quiz["correct"]:
                print("✅ 正解です！")
                score += 1
            else:
                print(f"❌ 不正解です。正解は {quiz['correct']} でした。")
                
        except ValueError:
            print("❌ 正しい数字を入力してください。")
    
    print(f"\n🎯 結果: {score}/{total_questions} 問正解！")
    percentage = (score / total_questions) * 100
    print(f"正答率: {percentage:.1f}%")
    
    if percentage >= 80:
        print("🏆 素晴らしい成績です！")
    elif percentage >= 60:
        print("👍 良い成績です！")
    else:
        print("💪 もう一度挑戦してみましょう！")

def word_guessing_game():
    """
    単語当てゲーム
    ヒントを参考に単語を当てるゲーム
    """
    print("\n" + "="*40)
    print("📝 単語当てゲーム")
    print("="*40)
    print("ヒントを参考に単語を当ててください！")
    
    # 単語とヒントのリスト
    words = [
        {"word": "りんご", "hint": "赤い果物"},
        {"word": "ねこ", "hint": "ペットとして人気の動物"},
        {"word": "ほし", "hint": "夜空に光るもの"},
        {"word": "みず", "hint": "透明な液体"},
        {"word": "ほん", "hint": "読むもの"}
    ]
    
    score = 0
    total_words = len(words)
    
    # 単語をシャッフル
    random.shuffle(words)
    
    for i, word_data in enumerate(words, 1):
        print(f"\n--- 問題 {i} ---")
        print(f"ヒント: {word_data['hint']}")
        
        answer = input("答えを入力してください: ").strip()
        
        if answer.lower() == word_data['word'].lower():
            print("✅ 正解です！")
            score += 1
        else:
            print(f"❌ 不正解です。正解は「{word_data['word']}」でした。")
    
    print(f"\n🎯 結果: {score}/{total_words} 問正解！")
    percentage = (score / total_words) * 100
    print(f"正答率: {percentage:.1f}%")

def show_menu():
    """
    ゲームメニューを表示
    """
    print("\n" + "="*50)
    print("🎮 簡単ゲーム集")
    print("="*50)
    print("1. 🎯 数当てゲーム")
    print("2. ✂️ じゃんけんゲーム")
    print("3. 🧠 簡単クイズゲーム")
    print("4. 📝 単語当てゲーム")
    print("0. 🚪 終了")
    print("="*50)

def main():
    """
    メイン関数
    ゲームの選択と実行を管理
    """
    print("🎮 簡単ゲーム集へようこそ！")
    print("楽しいゲームで遊びましょう！")
    
    while True:
        show_menu()
        
        try:
            choice = int(input("ゲームを選択してください (0-4): "))
            
            if choice == 0:
                print("🎮 ゲームを終了します。また遊んでね！")
                break
            elif choice == 1:
                number_guessing_game()
            elif choice == 2:
                rock_paper_scissors()
            elif choice == 3:
                simple_quiz()
            elif choice == 4:
                word_guessing_game()
            else:
                print("❌ 0-4の数字を入力してください。")
                continue
            
            # ゲーム終了後の処理
            input("\nEnterキーを押してメニューに戻ります...")
            
        except ValueError:
            print("❌ 正しい数字を入力してください。")
        except KeyboardInterrupt:
            print("\n\n🎮 ゲームを終了します。また遊んでね！")
            break

if __name__ == "__main__":
    main()
