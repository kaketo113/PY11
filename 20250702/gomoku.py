board_size = 15

def board_create():
    return [["・" for q in range(board_size)] for q in range(board_size)]

def board_print(board):
    print("   " + "".join([f"{i % 10:2}" for i in range(board_size)]))
    for i, row in enumerate(board):
        print(f"{i % 100:2}| " + " ".join(row))

def check_win(board, player):
    # 横方向のチェック
    for r in range(board_size):
        for c in range(board_size - 4):
            if all(board[r][c+i] == player for i in range(5)):
                return True

    # 縦方向のチェック
    for r in range(board_size - 4):
        for c in range(board_size):
            if all(board[r+i][c] == player for i in range(5)):
                return True

    # 右下がり斜め方向のチェック
    for r in range(board_size - 4):
        for c in range(board_size - 4):
            if all(board[r+i][c+i] == player for i in range(5)):
                return True

    # 左下がり斜め方向のチェック
    for r in range(board_size - 4):
        for c in range(4, board_size):
            if all(board[r+i][c-i] == player for i in range(5)):
                return True
                
    return False

def game_start():
    board = board_create()
    player = "○" 
    
    while True:
        print("\n" + "="*20)
        board_print(board)
        print(f"\n{player} のターンです。")

        # ユーザーからの入力を受け取る
        move = input("どこに置きますか？ (例: 7,8 のように行,列で入力): ")
        row_str, col_str = move.split(',')
        row, col = int(row_str), int(col_str)

            # 盤面に石を置く
        board[row][col] = player + " "

            # 勝利判定
        if check_win(board, player):
            board_print(board)
            print(f"\n {player} の勝ちです！ ")
            break

            # プレイヤーを交代する
        player = "✕" if player == "○" else "○"
game_start()