#○×ゲーム
a1 = "１"
b2 = "２"
c3 = "３"
d4 = "４"
e5 = "５"
f6 = "６"
g7 = "７"
h8 = "８"
i9 = "９"
print(f"{a1}|{b2}|{c3}")
print("--+--+--")
print(f"{d4}|{e5}|{f6}")
print("--+--+--")
print(f"{g7}|{h8}|{i9}")

owari = 9
while True: 
    a = input("どこに記号を入れる？(1から9)")
    if a == "1":
        a1 = a1.replace("１", "〇")
    if a == "2":
        b2 = b2.replace("２", "〇")
    if a == "3":
        c3 = c3.replace("３", "〇")
    if a == "4":
        d4 = d4.replace("４", "〇")
    if a == "5":
        e5 = e5.replace("５", "〇")
    if a == "6":
        f6 = f6.replace("６", "〇")
    if a == "7":
        g7 = g7.replace("７", "〇")
    if a == "8":
        h8 = h8.replace("８", "〇")
    if a == "9":
        i9 = i9.replace("９", "〇")

    print(f"{a1}|{b2}|{c3}")
    print("--+--+--")
    print(f"{d4}|{e5}|{f6}")
    print("--+--+--")
    print(f"{g7}|{h8}|{i9}")
    if  (a1==b2 and b2==c3) or (d4==e5 and e5==f6) or (g7==h8 and h8==i9) or (a1==d4 and d4==g7) or (b2==e5 and e5==h8) or (c3==f6 and f6==i9) or (a1==e5 and e5==i9) or (c3==e5 and e5==g7):
        print("〇の勝ち")
        break
    a = input("どこに記号を入れる？(1から9)")
    if a == "1":
        a1 = a1.replace("１", "× ")
    if a == "2":
        b2 = b2.replace("２", "× ")
    if a == "3":
        c3 = c3.replace("３", "× ")
    if a == "4":
        d4 = d4.replace("４", "× ")
    if a == "5":
        e5 = e5.replace("５", "× ")
    if a == "6":
        f6 = f6.replace("６", "× ")
    if a == "7":
        g7 = g7.replace("７", "× ")
    if a == "8":
        h8 = h8.replace("８", "× ")
    if a == "9":
        i9 = i9.replace("９", "× ")


    print(f"{a1}|{b2}|{c3}")
    print("--+--+--")
    print(f"{d4}|{e5}|{f6}")
    print("--+--+--")
    print(f"{g7}|{h8}|{i9}")
    if  (a1==b2 and b2==c3) or (d4==e5 and e5==f6) or (g7==h8 and h8==i9) or (a1==d4 and d4==g7) or (b2==e5 and e5==h8) or (c3==f6 and f6==i9) or (a1==e5 and e5==i9) or (c3==e5 and e5==g7):
        print("×の勝ち")
        break

    if a1 != "１" and b2 != "２" and c3 != "３" and d4 != "５" and f6 != "６" and g7 != "７" and h8 !="８" and i9 != "９":
        print("引き分け")
        break









