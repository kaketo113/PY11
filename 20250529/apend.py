gakusei = ["田中","谷分","三輪"]
print(gakusei[1])

#要素の追加
gakusei.append("竹内")
gakusei.append("井上")

for gaku in gakusei:
    print(gaku)

#要素の削除
gakusei.remove(2)
for gaku in gakusei:
    print(gaku)