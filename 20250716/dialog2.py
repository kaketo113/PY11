#dialog.py
#デスクトップアプリ起動サンプル
#GUI：グラフィカルユーザーインターフェース
#  ↕
#CUI：キャラクターユーザーインタフェース
import tkinter as tk

#ボタンが切り替わるようにしてみる
oshita = True

#ボタンを押したときの動作
def oshitaToki():
    global oshita #←これ大事
    if oshita == True :
        lbl.configure(text="本当に押したな")
        btn.configure(text="押すなって")
        oshita = False
    else:
        lbl.configure(text="父さんにも押されたことがないのに") 
        btn.configure(text="２回も押した")
        oshita = True

root = tk.Tk()
#ウィンドウサイズを設定 x←小文字のエックス
root.geometry("200x100")

#ラベル
lbl = tk.Label(text="押してみろよ")
#ボタン
btn = tk.Button(text="押せ！！", command = oshitaToki)

lbl.pack() #ラベルをウィンドウに配置
btn.pack() # ボタンをウィンドウに配置
tk.mainloop() #作ったウィンドウを表示する

