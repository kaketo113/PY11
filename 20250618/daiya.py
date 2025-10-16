def daiya():
    hen = int(input("一辺何個の三角形にしますか？"))
    for i in range(hen + 1):
        print(" " * (hen - i) + "* " * i)

    for i in range(hen-1, -1, -1):
        print(" " * (hen - i) + "* " * i)
daiya()