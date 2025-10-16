import random

class SudokuGame:
    """
    数独ゲームのメインクラス
    数独の生成、表示、入力処理、バリデーションを管理します
    """
    
    def __init__(self):
        """ゲームの初期化"""
        self.board_size = 9  # 数独は9x9のサイズ
        self.board = self.create_empty_board()  # 空のボードを作成
        self.original_board = None  # 初期状態のボードを保存（変更不可のセルを管理）
        self.generate_puzzle()  # 数独パズルを生成
    
    def create_empty_board(self):
        """
        空の9x9のボードを作成
        全てのセルを0（空）で初期化
        """
        return [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
    
    def print_board(self):
        """
        ボードを美しく表示
        3x3のボックスで区切り、プレイヤーが入力した数字は青色で表示
        """
        print("\n" + "="*50)
        print("数独ゲーム")
        print("="*50)
        
        # 9行分ループ
        for i in range(self.board_size):
            # 3行ごとに区切り線を表示
            if i % 3 == 0 and i != 0:
                print("-" * 35)
            
            row = ""
            # 9列分ループ
            for j in range(self.board_size):
                # 3列ごとに縦線を表示
                if j % 3 == 0 and j != 0:
                    row += "| "
                
                # セルの内容を表示
                if self.board[i][j] == 0:
                    row += " "  # 空のセルは空白で表示
                else:
                    if self.original_board[i][j] == 0:
                        # プレイヤーが入力した数字は青色で表示
                        row += f"\033[94m{self.board[i][j]}\033[0m "
                    else:
                        # 初期値は通常の色で表示
                        row += f"{self.board[i][j]} "
            
            print(f" {row}")
        
        print("="*50)
        print("入力形式: 行 列 数字 (例: 3 4 7)")
        print("終了: q")
        print("リセット: r")
        print("="*50)
    
    def is_valid_move(self, row, col, num):
        """
        指定した位置に数字を置けるかチェック
        数独のルール（行、列、3x3ボックスに同じ数字がない）を確認
        
        Args:
            row: 行番号（0-8）
            col: 列番号（0-8）
            num: 配置したい数字（1-9）
        
        Returns:
            bool: 配置可能ならTrue、不可能ならFalse
        """
        # 行のチェック：同じ行に同じ数字がないか確認
        for j in range(self.board_size):
            if self.board[row][j] == num:
                return False
        
        # 列のチェック：同じ列に同じ数字がないか確認
        for i in range(self.board_size):
            if self.board[i][col] == num:
                return False
        
        # 3x3のボックスのチェック：同じボックスに同じ数字がないか確認
        box_row = 3 * (row // 3)  # ボックスの開始行
        box_col = 3 * (col // 3)  # ボックスの開始列
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        
        return True  # 全てのチェックを通過
    
    def solve_sudoku(self, board):
        """
        数独を解く（バックトラッキングアルゴリズム）
        空のセルに1-9の数字を試して、有効な解答を見つける
        
        Args:
            board: 解く対象のボード
        
        Returns:
            bool: 解答が見つかったらTrue、見つからなかったらFalse
        """
        # 全てのセルを順番にチェック
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] == 0:  # 空のセルを見つけた
                    # 1-9の数字を順番に試す
                    for num in range(1, 10):
                        if self.is_valid_move(i, j, num):  # 数字を置けるかチェック
                            board[i][j] = num  # 数字を配置
                            # 再帰的に次のセルを解く
                            if self.solve_sudoku(board):
                                return True  # 解答が見つかった
                            board[i][j] = 0  # バックトラック：数字を削除
                    return False  # どの数字も置けない
        return True  # 全てのセルが埋まった
    
    def generate_puzzle(self):
        """
        数独パズルを生成
        1. 完全な数独を生成
        2. ランダムに数字を削除してパズルを作成
        """
        # 完全な数独を生成（バックトラッキングで解答を作成）
        self.solve_sudoku(self.board)
        
        # 元のボードを保存（初期値として変更不可にするため）
        self.original_board = [row[:] for row in self.board]
        
        # ランダムに数字を削除（難易度調整）
        cells_to_remove = 50  # 削除するセルの数（多いほど難しい）
        
        for _ in range(cells_to_remove):
            row = random.randint(0, 8)  # ランダムな行
            col = random.randint(0, 8)  # ランダムな列
            self.board[row][col] = 0  # 数字を削除（空にする）
    
    def is_board_full(self):
        """
        ボードが完成しているかチェック
        全てのセルに数字が入っているか確認
        
        Returns:
            bool: 完成していればTrue、未完成ならFalse
        """
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 0:  # 空のセルがあれば未完成
                    return False
        return True  # 全てのセルが埋まっている
    
    def is_solution_correct(self):
        """
        解答が正しいかチェック
        数独のルールに従っているか詳細に確認
        
        Returns:
            bool: 正しければTrue、間違っていればFalse
        """
        # 行のチェック：各行に1-9の数字が1つずつあるか確認
        for i in range(self.board_size):
            row_nums = set()  # 重複を避けるためにsetを使用
            for j in range(self.board_size):
                if self.board[i][j] in row_nums:  # 重複があれば不正
                    return False
                row_nums.add(self.board[i][j])
        
        # 列のチェック：各列に1-9の数字が1つずつあるか確認
        for j in range(self.board_size):
            col_nums = set()
            for i in range(self.board_size):
                if self.board[i][j] in col_nums:  # 重複があれば不正
                    return False
                col_nums.add(self.board[i][j])
        
        # 3x3ボックスのチェック：各ボックスに1-9の数字が1つずつあるか確認
        for box_row in range(0, 9, 3):  # ボックスの開始行（0, 3, 6）
            for box_col in range(0, 9, 3):  # ボックスの開始列（0, 3, 6）
                box_nums = set()
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if self.board[i][j] in box_nums:  # 重複があれば不正
                            return False
                        box_nums.add(self.board[i][j])
        
        return True  # 全てのチェックを通過
    
    def reset_board(self):
        """
        ボードを初期状態にリセット
        プレイヤーが入力した数字を全て削除して初期状態に戻す
        """
        self.board = [row[:] for row in self.original_board]
    
    def play(self):
        """
        ゲームを開始
        メインゲームループ：表示→入力→処理を繰り返す
        """
        while True:
            # 現在のボードを表示
            self.print_board()
            
            # 完成チェック
            if self.is_board_full():
                if self.is_solution_correct():
                    print("\n🎉 おめでとうございます！数独が完成しました！")
                else:
                    print("\n❌ 解答に誤りがあります。確認してください。")
                break
            
            try:
                # ユーザーからの入力を受け取る
                user_input = input("\n入力してください: ").strip().lower()
                
                # 特殊コマンドの処理
                if user_input == 'q':
                    print("ゲームを終了します。")
                    break
                elif user_input == 'r':
                    self.reset_board()
                    print("ボードをリセットしました。")
                    continue
                
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
                if self.original_board[row][col] != 0:
                    print("❌ このセルは変更できません（初期値）。")
                    continue
                
                # 有効な移動かチェック（数独のルールに従っているか）
                if not self.is_valid_move(row, col, num):
                    print("❌ この位置にその数字は置けません。")
                    continue
                
                # 数字を配置（全てのチェックを通過）
                self.board[row][col] = num
                print(f"✅ ({row+1}, {col+1}) に {num} を配置しました。")
                
            except ValueError:
                # 数値変換エラー（文字列を数値に変換できない場合）
                print("❌ 正しい数値を入力してください。")
            except KeyboardInterrupt:
                # Ctrl+Cでゲーム終了
                print("\n\nゲームを終了します。")
                break

def main():
    """
    メイン関数
    ゲームの説明と初期化を行う
    """
    print("数独ゲームへようこそ！")
    print("ルール: 各行、各列、各3x3ボックスに1-9の数字を1つずつ配置してください。")
    
    # ゲームインスタンスを作成して開始
    game = SudokuGame()
    game.play()

if __name__ == "__main__":
    main() 