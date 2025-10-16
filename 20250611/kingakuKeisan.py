import math
#金額計算関数
#def 関数名(※引数,引数＝デフォルト値≒初期値)
def kingakuKeisan(kigou, iro="指定なし"):
    #商品１から１０まで繰り返し表示する
    for n in range(1,11):
        #金額計算
        zeinuki = n * 100
        zeikomi = math.floor(zeinuki * 1.08)

        #表示
        # print("【大特価】商品:" + kigou, "サイズ:" str(n), "￥" + str(zeikomi),"色:" + iro)