from turtle import*
#亀の読み込み
shape("turtle")
#亀の登場
col = ["orange","lightgreen","gold","plum","tomato"]
#何色にする？
for i in range(5):
    #誤解繰り返し
    color(col[i])
    #丸に色を付ける
    circle(100)
    #半径100の円を描く
    left(72)
    #72度左を向く
done()
#終わり