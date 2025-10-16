def sikaku():
    hen = int(input("一辺何個の正方形にしますか？"))
    nuku = input("中を抜きますか？(y/n) ")

    if nuku == "y":
        nakanuki = int(input("どのくらいの大きさの正方形を抜く？ "))
    else:
        nakanuki = 0

    if nakanuki >= hen:
        print("中抜きのサイズが大きすぎるため、中抜きなしで描画します。")
        nakanuki = 0

    s_nuku = (hen - nakanuki) // 2
    e_nuku = s_nuku + nakanuki

    for tate in range(hen):
        for yoko in range(hen):
            if nuku == "y" and s_nuku <= tate < e_nuku and s_nuku <= yoko < e_nuku:
                print("　", end="")
            else:
                print("＊", end="")
        print()
sikaku()