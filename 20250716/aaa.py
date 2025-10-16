#五目並べ
def check_winner(board):
    # 縦のチェック
    for col in range(5):
        if all(board[row][col] == 'X' for row in range(5)):
            return 'X'
        if all(board[row][col] == 'O' for row in range(5)):
            return 'O'
    # 横のチェック
    for row in range(5):
        if all(board[row][col] == 'X' for col in range(5)):
            return 'X'
        if all(board[row][col] == 'O' for col in range(5)):
            return 'O'
    # 斜めのチェック
    if all(board[i][i] == 'X' for i in range(5)):
        return 'X'
    if all(board[i][i] == 'O' for i in range(5)):
        return 'O'
    if all(board[i][4-i] == 'X' for i in range(5)):
        return 'X'
    if all(board[i][4-i] == 'O' for i in range(5)):
        return 'O'
    return None
# 盤面の初期化
board = [[' ' for _ in range(5)] for _ in range(5)]
current_player = 'X'
while True:
    # 盤面の表示
    for row in board:
        print('|'.join(row))
        print('-' * 9)
    # プレイヤーの入力
    move = input(f"Player {current_player}, enter your move (row and column): ")
    row, col = map(int, move.split())
    if board[row][col] != ' ':
        print("Invalid move. Try again.")
        continue
    board[row][col] = current_player
    winner = check_winner(board)
    if winner:
        for row in board:
            print('|'.join(row))
            print('-' * 9)
        print(f"Player {winner} wins!")
        break
    current_player = 'O' if current_player == 'X' else 'X'
import os
import TkEasyGUI as eg
#初期フォルダとしてデスクトップを指定
desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
#ファイル選択ダイアログを表示する
path = eg.popup_get_file(
    title="処理対象のファイルを選択",
    initial_folder=desktop_dir)
print(path)
