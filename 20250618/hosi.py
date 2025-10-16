def hosi():
    sankaku = 3
    t = 0
    for i in range(sankaku):
        k = 1 + 2 * i
        j = sankaku * sankaku - i * 2
        print(" " *(j) + "＊" * (k))
        i = i + 1
    for q in range(sankaku + 1):
        print(" " * q + "＊" * (sankaku * sankaku + 1 - q))
    for w in range(sankaku):
        r = 1 + 2 * w
        print(" " * (sankaku - t) + "＊" * (sankaku - t) + "　" * (r + t) + "＊" * (sankaku - t))
        t = t + 1
        if w == 1:
            break
hosi()






