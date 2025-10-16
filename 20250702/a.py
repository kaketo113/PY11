gakuseiTachi = [
    ["12","50493","新海","尊琉","シンカイ","タケル"],
    ["06","50103","岩田","直也","イワタ","ナオヤ"],
    ["30","50074","又吉","奏帆","マタヨシ","カナホ"],
    ["10","50572","河原","諒晟","カワハラ","リョウセイ"],
    ["06","50615","井上","陽輝","イノウエ","ハルキ"],
    ["11","50412","菅沼","迦音","スガヌマ","カノン"],
    ["29","50197","溝口","翔斗","ミゾグチ","カケト"],
    ["30","50675","満","颯太","ミツ","ソウタ"],
    ["15","50743","髙松","航太","タカマツ","コウタ"],
]
#あなたのデータを
#出席番号　姓　名　学籍番号
#の順番で表示する
# print(gakuseiTachi[0][0],gakuseiTachi[0][2],gakuseiTachi[0][3],gakuseiTachi[0][1])#[0][0]の一つ目の[0]は一つ目の[]内の中での番号で二つ目の[0]は[]の中の[]の番号
# print(gakuseiTachi[1][0],gakuseiTachi[1][2],gakuseiTachi[1][3],gakuseiTachi[1][1])
 
# print("＊＊＊＊ここから繰り返し！！＊＊＊＊")
# #２.配列を繰り返し処理で活用
 
# for gakusei in gakuseiTachi:
#     print(gakusei[0],gakusei[2],gakusei[3],gakusei[1])
 
 
for gakusei in gakuseiTachi:
    if len(gakusei[2])==1:
        print(gakusei[0],gakusei[2],end="　|")
    if len(gakusei[2])==2:
        print(gakusei[0],gakusei[2],end="|")
    if gakusei == gakuseiTachi:
        for gakusei in gakuseiTachi:
            print("　",gakusei[3],end="|")
