import random

def cr_board():
    return [[0 for _ in range(9)] for _ in range(9)]
def pr_board(board):

    print()
    print("数独ゲーム")
    print()

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 23)
        
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "| "
            
            if board[i][j] == 0:
                row += "  "
            else:
                row += f"{board[i][j]} "
        
        print(f" {row}")
    
    print()
    print("入力例: 3 4 7 (3行目4列目に7を入れる)")
    print("終了: q")
    print()

def haiti():
    for i in range(9):