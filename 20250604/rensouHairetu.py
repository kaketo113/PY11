#rensouHairetu.py
#配列
sensei =["髙橋","真広"]
#連想配列
chikokuma = {"苗字":"仲田","名前":"ゆうじ"}

print("先生は",sensei[0],sensei[1],"です")
print("遅刻魔は",chikokuma["苗字"],chikokuma["名前"],"です")

#二次元配列
iinchou = [["岩田","綺華"],["中山","駿"],["藤浦","晃士"]]
alpha   = [{"苗字":"池田","名前":"峰皐"},{"苗字":"井上","名前":"陽輝"}]

print("委員長１人目は",iinchou[0][0],iinchou[0][1],"です")
print("委員長２人目は",iinchou[1][0],iinchou[1][1],"です")
print("委員長３人目は",iinchou[2][0],iinchou[2][1],"です")

print("アルファ委員１人目は",alpha[0]["苗字"],alpha[0]["名前"],"です")
print("アルファ委員２人目は",alpha[1]["苗字"],alpha[1]["名前"],"です")
