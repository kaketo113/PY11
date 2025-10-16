#0 import
#1 jadge機能
    #1-1 get_jadge関数
    #1-2 月日の所得
    #1-3 言語判定を引数変換
    #1-4 seizaHantei関数呼び出し
    #1-5 結果を画面に反映
#2 子module
    #2-1 create_window関数
    #2-2 sub_window生成
    #2-3 ラベルの追加
    #2-4 入力欄の追加
        #2-4-1 月の入力欄
        #2-4-1 日の入力欄
        #2-4-1 言語の選択欄
    #2-5 判定ボタンの追加
    #2-6 結果表示欄
    #2-7 親ウィンドウを操作不能にする  
#4 main処理
    #4-1 親ウィンドウ生成
    #4-2 ウィジェット変数のグローバル化
    #4-3 ウィジェット変数の初期化
    #4-4 子画面インスタンス変数をGlobal化するための初期化
    #4-5 ラベルの追加
    #4-6 星座判定ボタンの追加
    #4-7 終了ボタンの追加
#4 機能追加で加点

#0 import
import ctypes
import tkinter
from tkinter import ttk
from tkinter import messagebox
import seizaHantei as sh
from PIL import Image, ImageTk


#1 jadge機能
#1-1 get_jadge関数
def get_jadge():
    try:

    #1-2 月日の取得
        month = int(w_month.get())
        day = int(w_day.get())
        lang = w_lang.get()

    #1-3 言語判定などを引数変換
        lang_code = "ja" if lang == "日本語" else "en"

    #1-4 seizaHantei関数呼び出し
        result = sh.seiza(month, day)

    #1-5 結果を画面に反映
        mes =result[lang_code]
        w_res.set(f"あなたの星座は\n{mes}です")
    except ValueError:

        # 数字以外の入力や空欄の場合のエラー処理
        messagebox.showerror("入力エラー", "月と日を半角数字で正しく入力してください。")
    except Exception as e:

        # その他の予期せぬエラー処理
        messagebox.showerror("エラー", f"エラーが発生しました: {e}")


#2 子module

#2-1 create_window関数
def create_window():

    #2-2 sub_window生成
    global sub_window

    sub_window = tkinter.Toplevel(root)
    sub_window.title("星座判定")
    sub_window.geometry("800x600")

    #4 機能追加
    try:
        image_path = "C:/Users/tama/Desktop/HAL2025/PY11/20250903/bg-star01.jpg"

        # Pillowを使って画像を開く
        bg_image = Image.open(image_path)
        bg_image = ImageTk.PhotoImage(bg_image)

        bg_label = tkinter.Label(sub_window, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 画像が参照され続けるようにする
        bg_label.image = bg_image

    except Exception as e:
        messagebox.showerror("エラー", f"画像の読み込みに失敗しました: {e}")
        return

    #2-3 ラベルの追加
    tkinter.Label(
        sub_window,
        text="　　　　星座判定　　　　",
        font=("Segoe UI Semibold","20","bold")
    ).place(x=200, y=10)

    #2-4 入力欄の追加
    
    #2-4-1 月の入力欄
    tkinter.Label(sub_window, text="生まれた月", font=("Segoe UI Semibold", "16", "bold")).place(x=230, y=75)
    tkinter.Entry(
        sub_window, textvariable=w_month, width=3,
        font=("Segoe UI Semibold", 16), justify="center"
    ).place(x=380, y=75)
    tkinter.Label(sub_window, text="月", font=("Segoe UI Semibold", "16", "bold")).place(x=430, y=75)
    
    #2-4-2 日の入力欄
    tkinter.Label(sub_window, text="生まれた日", font=("Segoe UI Semibold", "16", "bold")).place(x=230, y=105)
    tkinter.Entry( 
        sub_window, textvariable=w_day, width=3,
        font=("Segoe UI Semibold", 16), justify="center"
    ).place(x=380, y=105)
    tkinter.Label(sub_window, text="日", font=("Segoe UI Semibold", "16", "bold")).place(x=430, y=105)
    
    #2-4-1 言語の選択欄
    tkinter.Label(sub_window, text="言語選択", font=("Segoe UI Semibold", "16", "bold")).place(x=230, y=140)
    combo_lang = ttk.Combobox(
        sub_window, textvariable=w_lang, values=["日本語", "English"],
        state="readonly", font=("Segoe UI Semibold", 14)
    )
    combo_lang.place(x=380, y=145)
    combo_lang.set("日本語") # 初期値を設定

    #2-5 判定ボタンの追加
    tkinter.Button(
        sub_window, text="判定", width=20, height=1,
        font=("Segoe UI Semibold","20","bold"), command=get_jadge
    ).place(x=200, y=200)

    #2-6 結果表示欄
    tkinter.Label(
        sub_window, textvariable=w_res, font=("Segoe UI Semibold", "24", "bold"),
        bg="lightyellow", width=25, height=4, justify="center"
    ).place(x=160, y=280)

    #4戻るボタンの追加  
    tkinter.Button(
        sub_window,
        text="戻る",
        width=10,
        height=2,
        font=("Segoe UI Semibold", "16", "bold"),
        command=sub_window.destroy
    ).place(x=650, y=520) 


    #2-7 親ウィンドウを操作不能にする  
    sub_window.grab_set()

# 4-1 追加機能
def create_window2():
    global sub_window2

    sub_window2 = tkinter.Toplevel(root)
    sub_window2.title("○×ゲーム")
    sub_window2.geometry("800x600")


    #4 機能追加
    try:
        image_path = "C:/Users/tama/Desktop/HAL2025/PY11/20250903/bg-marubatu01.jpg"

        # Pillowを使って画像を開く
        bg_image = Image.open(image_path)
        bg_image = ImageTk.PhotoImage(bg_image)

        bg_label = tkinter.Label(sub_window2, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 画像が参照され続けるようにする
        bg_label.image = bg_image

    except Exception as e:
        messagebox.showerror("エラー", f"画像の読み込みに失敗しました: {e}")
        return
    
    # 盤面とターン
    board = [""] * 9
    turn = ["○"]  # リストでラップして参照可能に

    #勝利判定
    def check_winner():
        win = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for line in win:
            a,b,c = line
            if board[a] and board[a]==board[b] and board[b]==board[c]:
                return board[a]
        if all(board):
            return "引き分け"
        return None
    
    #○×をおく機能
    def click(nakami):

        # すでに置かれているか、勝者が決まっている場合は無視
        if board[nakami] or check_winner():
            return
        board[nakami] = turn[0] #その時のターンの人の記号を置く
        buttons[nakami].config(text=turn[0]) #その時のターンの人の記号にボタンの表示を変える

        # 勝利判定
        winner = check_winner()
        if winner:

            # 勝者が決まった場合の処理
            result.set(f"{winner}の勝ち！" if winner in ["○","✕"] else "引き分け！")
        else:

            # ターンを交代
            turn[0] = "✕" if turn[0]=="○" else "○"
            result.set(f"{turn[0]}の番です")

    
    buttons = []

    # 9個のボタンを配置
    for i in range(9):
        btn = tkinter.Button( 
            sub_window2,
            text="",
            width=6,
            height=2,
            font=("Segoe UI Semibold", "32", "bold"),
            command=lambda nakami=i: click(nakami)
        )

        # ボタンを3×3で配置
        btn.place(x=200 + (i%3)*150, y=100 + (i//3)*150)

        # ボタンをリストに追加
        buttons.append(btn)

    # ターン表示ラベル
    result = tkinter.StringVar()
    result.set("〇の番です")
    tkinter.Label(
        sub_window2, 
        textvariable=result,
        font=("Segoe UI Semibold", "20", "bold"),
        bg="lightyellow", 
        width=20, 
        height=2
    ).place(x=250, y=10)
    
    #戻るボタン
    tkinter.Button(
        sub_window2, text="戻る", width=10, height=2,
        font=("Segoe UI Semibold", "16", "bold"),
        command=sub_window2.destroy
    ).place(x=665, y=510)

    sub_window2.grab_set()

#4 main処理
if __name__ == "__main__":

    #4-1 親ウィンドウ生成
    root =tkinter.Tk()
    root.title("アプリメニュー")
    root.geometry("800x600")

    # 4 機能追加
    try:
        image_path = "C:/Users/tama/Desktop/HAL2025/PY11/20250903/bg-sakura01.jpg"

        # Pillowを使って画像を開く
        bg_image = Image.open(image_path)
        bg_image = ImageTk.PhotoImage(bg_image)

        bg_label = tkinter.Label(root, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 画像が参照され続けるようにする
        bg_label.image = bg_image

    except Exception as e:
        messagebox.showerror("エラー", f"画像の読み込みに失敗しました: {e}")
        exit(1)

    #4-2 ウィジェット変数のグローバル化
    global w_month #入力された月
    global w_day #入力された日
    global w_lang #表示言語
    global w_res #判定した星座

    #4-3 ウィジェット変数の初期化

    w_month = tkinter.StringVar()
    w_month.set('')
    w_day = tkinter.StringVar()
    w_day.set('')
    w_lang = tkinter.StringVar()
    w_lang.set('')
    w_res = tkinter.StringVar()
    w_res.set('')

    #4-4子画面インスタンス変数をGlobal化するための初期化
    sub_win = None

    #4-5 親画面の画面上にタイトルを表示するラベルの配置
    l = tkinter.Label(
        root,
        text = "アプリメニュー",
        font=("Segoe UI Semibold", "20", "bold")
    ).place(x=10,y=10)

    #4-6 親画面の画面上に、アプリケーション１のボタンを配置
    b1 = tkinter.Button(
        root, 
        text="星座判定", 
        width=30, 
        height=2, 
        font=("Segoe UI Semibold", "20", "bold"), 
        #command=show_sub_window(root)
        command=create_window #commandはボタンを押したときの動作（今回は子ウィンドウ表示関数）
    ).place(x=150,y=100)

    #親画面の画面上に、アプリケーション2のボタンを配置
    b2 = tkinter.Button(
        root,
        text="○×ゲーム",
        width=30,
        height=2,
        font=("Segoe UI Semibold", "20", "bold"),
        command=create_window2
    ).place(x=150,y=240)

    #4-7 終了ボタンの追加
    b4 = tkinter.Button(
        root,
        text="終了",
        width=7, 
        height=1, 
        font=("Segoe UI Semibold", "20", "bold"), 
        command=root.quit
    ).place(x=630,y=520)

    root.mainloop()
