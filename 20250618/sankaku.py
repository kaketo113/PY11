def sankaku():
    """
    三角形を描画する関数
    """
    hen = int(input("一辺何個の三角形にしますか？"))
    for i in range(hen+1):
        print("*"*i)
    print("*"*(i+1))
    for i in range(hen,-1,-1):
        print("*"*i)
    for i in range(hen,-1,-1):
        print(" "*(hen-i+1)+"*"*i)
sankaku()