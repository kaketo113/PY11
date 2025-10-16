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

# 1秒ごとに次の音を鳴らす（順→逆→順…）
current_index = {'idx': 0}
direction = {'forward': True}
extra_c_flag = {'pending': False}

# 逆順開始時にC2から始めるためのフラグ
reverse_start_flag = {'pending': False}

def play_next():
    # 逆順開始時は必ずC2から
    if reverse_start_flag['pending']:
        sounds['C2'].play()
        current_index['idx'] = len(notes) - 2  # C2の次はB
        direction['forward'] = False
        reverse_start_flag['pending'] = False
    elif extra_c_flag['pending']:
        sounds['C'].play()
        extra_c_flag['pending'] = False
    else:
        idx = current_index['idx']
        sounds[notes[idx]].play()
        if direction['forward']:
            current_index['idx'] += 1
            if current_index['idx'] >= len(notes):
                # 順方向の端に到達したらCを鳴らして逆方向へ
                current_index['idx'] = len(notes) - 1
                direction['forward'] = False
                extra_c_flag['pending'] = True
                reverse_start_flag['pending'] = True
        else:
            current_index['idx'] -= 1
            if current_index['idx'] < 0:
                # 逆方向の端に到達したらCを鳴らして順方向へ
                current_index['idx'] = 0
                direction['forward'] = True
                extra_c_flag['pending'] = True
    root.after(1000, play_next)

root.after(1000, play_next)  # 最初の呼び出し

root.mainloop()