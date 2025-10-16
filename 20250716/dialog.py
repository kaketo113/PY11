#dialog.py
#デスクトップアプリ起動サンプル
#GUI:グラフィカルユーザーインターフェース↔CUI:キャラクターユーザーインターフェース
import TkEasyGUI as eg
ans = eg.popup_yes_no("ラーメンは好きですか？")
if ans == "Yes":
    eg.popup_ok("同意 - 僕も好きです。")
else:
    eg.popup_ok("本当？ - まさか、ラーメンが嫌いだなんて！")

