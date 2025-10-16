def roku():
    hen = int(input("一辺何個の正六角形にしますか？"))

    for i in range(hen):
        print(" " * (hen - i - 1) + "＊" * (hen + i))

    for i in range(hen - 2,-1,-1):#range(start(開始位置),stop(設定した数値より大きい間繰り返す),step(iを設定した値ずつ減らす))
        print(" " * (hen - i - 1) + "＊" * (hen + i))
roku()