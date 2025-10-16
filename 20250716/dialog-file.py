import os
import TkEasyGUI as eg

#初期フォルダとしてデスクトップを指定
desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
#ファイル選択ダイアログを表示する
path = eg.popup_get_file(
    title="処理対象のファイルを選択",
    initial_folder=desktop_dir)
print(path)