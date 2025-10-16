#文字列操作

#１　型変換
kotae  =  1000  +  10
kotae2 = "1000" +  str(10)
kotae3 = "1000" + "10"

print("答え１",kotae)
print("答え２",kotae2)
print("答え３",kotae3)

#２　文字列抽出
name= "髙橋真広"
print("名前:",name)
print("二文字目",name[1])
print("三文字目以降",name[2:])
print("2-3文字目",name[1:3])
 
#３　分割(ほかの言語でもsplit)
ymd = "2025/06/04"
nengappi = ymd.split("/")#区切りたい文字を指定する
print("年",nengappi[0])
print("月",nengappi[1])
print("日",nengappi[2])

#文字列の長さ(他言語ではlengthやsize)
nagasa = len("私は何文字でしょう")
print("文字数",nagasa)
ymdNoNagasa = len(ymd)
print("変数の長さ",ymdNoNagasa)

print("彼らの幅を統一したい")
sankyoudai = ["林","藤浦","日比野"]
for name in sankyoudai:
    print((name+"　　　")[:3],end="|")
print()

suchi=[1,10,100]
for kazu in suchi:
    print(("000" + str(kazu))[-3:])