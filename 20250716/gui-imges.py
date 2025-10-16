from PIL import Image, ImageOps
import TkEasyGUI as eg

#画面レイアウトを定義
layout = [
    [eg.Button("画像ファイルを選択")],
    [eg.Image(key="image1"),eg.Image(key="image2")],
]

#ウィンドウを開始してイベントループを開始
window = eg.Window("画像ネガポジ反転ツール",layout)
while window.is_alive():
    event, value = window.read()
    if event == "画像ファイルを選択":
        image_file = eg.popup_get_file(title ="画像ファイルを選択")
        try:
            img = Image.open(image_file)
        except Exception as e:
            eg.popup_ok(f"画像ファイルを読み取れません\n{e}")
            continue
        inverted_img = ImageOps.invert(img.convert("RGB"))
        out_file = image_file + "-inverted.png"
        inverted_img.save(out_file)
        window["image1"].update(data=img)
        window["image2"].update(data=inverted_img)
        eg.popup_ok(f"ネガポジを反転した画像を保存しました\n{out_file}")