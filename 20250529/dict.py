#辞書型

#今まで
takahashi = ["髙橋","真広","先生"]
print(takahashi[0])
print(takahashi[1])

#辞書
masahiro = {"苗字":"髙橋","名前":"真広","職業":"先生"}
print(masahiro["苗字"])
print(masahiro["名前"])
print(masahiro["職業"])

#二次元配列
ningen = [masahiro]
ningen.append({"苗字":"藤浦","名前":"晃士","職業":"委員長"})
ningen.append({"苗字":"日比野","名前":"優亜","職業":"副委員長"})

for hito in ningen:
    print("苗字:",hito["苗字"])