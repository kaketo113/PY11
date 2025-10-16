inu = False
neko = False

if inu == True and neko == True:
    print("動物好き", end=" ")
elif inu == True:
        print("犬好き",end="")
elif neko == True:
        print("猫好き",end="")
if inu == False and neko == False:
    print("動物嫌い",end="")

print("なのですね")

if inu == True or neko == True:
    print("私もです")
elif inu == False and neko == False:
    print("がっかりです。")