import tkinter as tk
import pygame

# 初期化
pygame.init()
pygame.mixer.init()

# 音の読み込み
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C2']
sounds = {note: pygame.mixer.Sound(f"sounds/{note}.wav") for note in notes}

# 音を鳴らす関数
def play_note(note):
    def inner():
        sounds[note].play()
    return inner

# Windowsの作成
#tkinterをインスタンス化
root = tk.Tk()
# ウィンドウサイズ指定
root.geometry("640x150")
# ウィンドウタイトル指定
root.title("Python Piano")

# note配列の要素数分のボタンを配置
for i, note in enumerate(notes):
    btn = tk.Button(root, text=note, width=8, height=5, command=play_note(note))
    btn.place(x=i*80, y=0)

root.mainloop()