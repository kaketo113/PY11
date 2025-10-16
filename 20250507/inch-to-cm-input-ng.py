# 入力を得てインチをセンチメートルに変換
# 変数のもとになる値
per_inch = 2.54
#　ユーザーから入力を得る
inch_str = input("inch ")
# 型変換 文字列　→　小数点数
inch = float(inch_str)
# 計算
cm = inch * per_inch
# 結果を表示
desc = "{0}inch = {1}cm".format(inch,cm)
print(desc)