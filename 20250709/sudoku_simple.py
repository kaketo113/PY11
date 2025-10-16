import random

def create_board():
    """
    空の9x9ボードを作成
    全てのセルを0（空）で初期化して数独の盤面を準備
    """
    return [[0 for _ in range(9)] for _ in range(9)]

def print_board(board):
    """
    ボードを美しく表示
    3x3のボックスで区切って見やすく表示する
    """
    print("\n" + "="*40)
    print("数独ゲーム")
    print("="*40)
    
    # 9行分ループして各行を表示
    for i in range(9):
        # 3行ごとに区切り線を表示（見やすくするため）
        if i % 3 == 0 and i != 0:
            print("-" * 30)
        
        row = ""
        # 9列分ループして各セルを表示
        for j in range(9):
            # 3列ごとに縦線を表示（3x3ボックスを区切る）
            if j % 3 == 0 and j != 0:
                row += "| "
            
            # セルの内容を表示
            if board[i][j] == 0:
                row += "  "  # 空のセルは空白で表示
            else:
                row += f"{board[i][j]} "  # 数字があるセルは数字を表示
        
        print(f" {row}")
    
    print("="*40)
    print("入力例: 3 4 7 (3行目4列目に7を入れる)")
    print("終了: q")
    print("="*40)

def is_valid(board, row, col, num):
    """
    数字を置けるかチェック
    数独のルール（行、列、3x3ボックスに同じ数字がない）を確認
    
    Args:
        board: 現在のボード
        row: 行番号（0-8）
        col: 列番号（0-8）
        num: 配置したい数字（1-9）
    
    Returns:
        bool: 配置可能ならTrue、不可能ならFalse
    """
    # 行のチェック：同じ行に同じ数字がないか確認
    for j in range(9):
        if board[row][j] == num:
            return False
    
    # 列のチェック：同じ列に同じ数字がないか確認
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # 3x3ボックスのチェック：同じボックスに同じ数字がないか確認
    box_row = 3 * (row // 3)  # ボックスの開始行
    box_col = 3 * (col // 3)  # ボックスの開始列
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True  # 全てのチェックを通過

def solve_sudoku(board):
    """
    数独を解く（バックトラッキングアルゴリズム）
    空のセルに1-9の数字を試して、有効な解答を見つける
    
    Args:
        board: 解く対象のボード
    
    Returns:
        bool: 解答が見つかったらTrue、見つからなかったらFalse
    """
    # 全てのセルを順番にチェック
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 空のセルを見つけた
                # 1-9の数字を順番に試す
                for num in range(1, 10):
                    if is_valid(board, i, j, num):  # 数字を置けるかチェック
                        board[i][j] = num  # 数字を配置
                        # 再帰的に次のセルを解く
                        if solve_sudoku(board):
                            return True  # 解答が見つかった
                        board[i][j] = 0  # バックトラック：数字を削除
                return False  # どの数字も置けない
    return True  # 全てのセルが埋まった

def generate_puzzle():
    """
    簡単な数独パズルを生成
    1. 完全な数独を生成
    2. ランダムに数字を削除してパズルを作成
    
    Returns:
        tuple: (パズルボード, 元の完全なボード)
    """
    # 完全な数独を作成（バックトラッキングで解答を作成）
    board = create_board()
    solve_sudoku(board)
    
    # 元のボードを保存（初期値として変更不可にするため）
    original = [row[:] for row in board]
    
    # 簡単な難易度（30個の数字を残す）
    cells_to_remove = 51  # 削除するセルの数（多いほど難しい）
    
    # ランダムに数字を削除
    for _ in range(cells_to_remove):
        row = random.randint(0, 8)  # ランダムな行
        col = random.randint(0, 8)  # ランダムな列
        board[row][col] = 0  # 数字を削除（空にする）
    
    return board, original

def is_complete(board):
    """
    ボードが完成しているかチェック
    全てのセルに数字が入っているか確認
    
    Args:
        board: チェックするボード
    
    Returns:
        bool: 完成していればTrue、未完成ならFalse
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 空のセルがあれば未完成
                return False
    return True  # 全てのセルが埋まっている

def check_solution(board):
    """
    解答が正しいかチェック
    数独のルールに従っているか詳細に確認
    
    Args:
        board: チェックするボード
    
    Returns:
        bool: 正しければTrue、間違っていればFalse
    """
    # 行のチェック：各行に1-9の数字が1つずつあるか確認
    for i in range(9):
        if len(set(board[i])) != 9:  # setで重複を除去して9個あるかチェック
            return False
    
    # 列のチェック：各列に1-9の数字が1つずつあるか確認
    for j in range(9):
        col = [board[i][j] for i in range(9)]  # 列の数字を取得
        if len(set(col)) != 9:  # setで重複を除去して9個あるかチェック
            return False
    
    # 3x3ボックスのチェック：各ボックスに1-9の数字が1つずつあるか確認
    for box_row in range(0, 9, 3):  # ボックスの開始行（0, 3, 6）
        for box_col in range(0, 9, 3):  # ボックスの開始列（0, 3, 6）
            box = []
            # 3x3ボックス内の全ての数字を取得
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    box.append(board[i][j])
            if len(set(box)) != 9:  # setで重複を除去して9個あるかチェック
                return False
    
    return True  # 全てのチェックを通過

def play_sudoku():
    """
    数独ゲームを開始
    メインゲームループ：表示→入力→処理を繰り返す
    """
    print("数独ゲームへようこそ！")
    print("ルール: 各行、各列、各3x3ボックスに1-9の数字を1つずつ配置してください。")
    
    # パズルを生成
    board, original = generate_puzzle()
    
    # メインゲームループ
    while True:
        # 現在のボードを表示
        print_board(board)
        
        # 完成チェック
        if is_complete(board):
            if check_solution(board):
                print("\n🎉 おめでとうございます！数独が完成しました！")
            else:
                print("\n❌ 解答に誤りがあります。")
            break
        
        # ユーザー入力の処理
        try:
            # ユーザーからの入力を受け取る
            user_input = input("\n入力してください: ").strip()
            
            # 終了コマンドの処理
            if user_input.lower() == 'q':
                print("ゲームを終了します。")
                break
            
            # 入力の解析：行 列 数字 の形式で分割
            parts = user_input.split()
            if len(parts) != 3:
                print("❌ 正しい形式で入力してください: 行 列 数字")
                continue
            
            # 文字列を数値に変換（インデックスは0から始まるので-1）
            row = int(parts[0]) - 1
            col = int(parts[1]) - 1
            num = int(parts[2])
            
            # 入力値の範囲チェック
            if not (0 <= row <= 8 and 0 <= col <= 8):
                print("❌ 行と列は1-9の範囲で入力してください。")
                continue
            
            if not (1 <= num <= 9):
                print("❌ 数字は1-9の範囲で入力してください。")
                continue
            
            # 初期値のセルは変更不可
            if original[row][col] != 0:
                print("❌ このセルは変更できません（初期値）。")
                continue
            
            # 有効な移動かチェック（数独のルールに従っているか）
            if not is_valid(board, row, col, num):
                print("❌ この位置にその数字は置けません。")
                continue
            
            # 数字を配置（全てのチェックを通過）
            board[row][col] = num
            print(f"✅ ({row+1}, {col+1}) に {num} を配置しました。")
            
        except ValueError:
            # 数値変換エラー（文字列を数値に変換できない場合）
            print("❌ 正しい数値を入力してください。")
        except KeyboardInterrupt:
            # Ctrl+Cでゲーム終了
            print("\n\nゲームを終了します。")
            break

if __name__ == "__main__":
    play_sudoku() 