# 五目並べゲームの盤面サイズ（15×15）
board_size = 15

def board_create():
    """
    15×15の空の盤面を作成する関数
    全てのマスを「・」で初期化
    """
    return [["・" for r in range(board_size)] for r in range(board_size)]

def board_print(board):
    """
    盤面を美しく表示する関数
    列番号と行番号を表示し、各マスの状態を表示
    """
    # 列番号を表示（0-14）
    print("   " + " ".join([f"{i:>2}" for i in range(board_size)]))
    # 各行を表示（行番号 + 各マスの状態）
    for i, gyou in enumerate(board):  # enumerate: リストの要素とインデックス（番号）を同時に取得
        print(f"{i:2}| " + " ".join(gyou))

def check_win(board, player):
    """
    指定されたプレイヤーが勝利しているかを判定する関数
    横、縦、斜め（右下がり・左下がり）の4方向で5つ並んでいるかをチェック
    """
    
    # 横方向のチェック（同じ行で5つ並んでいるか）
    for g in range(board_size):           # 各行について
        for r in range(board_size - 4):   # 開始位置（5つ並ぶ余地がある位置）
            win = True
            for i in range(5):            # 5マス分チェック
                if board[g][r+i] != (player + " "):  # プレイヤーの石でない場合
                    win = False
                    break
            if win:  # 5つ並んでいた場合
                return True

    # 縦方向のチェック（同じ列で5つ並んでいるか）
    for g in range(board_size - 4):       # 開始行（5つ並ぶ余地がある行）
        for r in range(board_size):       # 各列について
            win = True
            for i in range(5):            # 5マス分チェック
                if board[g+i][r] != (player + " "):  # プレイヤーの石でない場合
                    win = False
                    break
            if win:  # 5つ並んでいた場合
                return True

    # 右下がり斜め方向のチェック（行と列が同時に増加）
    for g in range(board_size - 4):
        for r in range(board_size - 4):
            win = True
            for i in range(5):
                if board[g+i][r+i] != (player + " "):  # プレイヤーの石でない場合
                    win = False
                    break
            if win:  # 5つ並んでいた場合
                return True

    # 左下がり斜め方向のチェック（行は増加、列は減少）
    for g in range(board_size - 4):
        for r in range(4, board_size):    # 列は4から開始（5つ並ぶ余地がある位置）
            win = True
            for i in range(5):
                if board[g+i][r-i] != (player + " "):  # プレイヤーの石でない場合
                    win = False
                    break
            if win:  # 5つ並んでいた場合
                return True
                
    return False  # どの方向でも5つ並んでいない場合

def full(board):
    """
    盤面が全て埋まっているか（引き分けか）を判定する関数
    「・」が残っていればFalse、全て埋まっていればTrue
    """
    for gyou in board:
        if "・" in gyou:  # 空のマスが残っている場合
            return False
    return True  # 全て埋まっている場合

def game_start():
    """
    五目並べゲームのメインループ
    プレイヤーが交互に石を置き、勝利判定を行う
    """
    board = board_create()  # 空の盤面を作成
    player = "○"           # 最初のプレイヤー
    
    while True:
        print()  # 空行を出力
        board_print(board)  # 現在の盤面を表示
        print(f"\n{player} のターンです。")

        # ユーザーからの入力を受け取る（行,列の形式）
        oku = input("どこに置きますか？ (例: 7,8 のように行,列で入力): ")
        gyou, retu = oku.split(',')  # カンマで分割
        gyou, retu = int(gyou), int(retu)  # 文字列を整数に変換

        # 盤面に石を置く
        board[gyou][retu] = (player + " ")

        # 勝利判定
        if check_win(board, player):
            board_print(board)  # 最終盤面を表示
            print(f"\n {player} の勝ちです！ ")
            break

        # プレイヤーを交代する（○と☓を交互に）
        player = "☓" if player == "○" else "○"
game_start()