import random
kuji = ["大吉","中吉","凶","絶望的なほどの凶"]

print( random.choice(kuji))

seiza = ["おひつじ座","おうし座","ふたご座","かに座","しし座","おとめ座","てんびん座","さそり座","いて座","やぎ座","みずがめ座","うお座"]

for s in seiza:
    print(s)
    if s == "かに座":
        print("キャンサー")