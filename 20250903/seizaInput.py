from seizaHantei import seiza


tanjyou = input("誕生日を半角数字4桁で入力して")

month = int(tanjyou[0:2])
day   = int(tanjyou[2:4])

seiza1 = seiza(month,day)
while True:
        lang = input("表示言語を選んでください (1: 日本語, 2: English) ")
        if lang == '1':
            print(f"\nあなたの星座は {seiza1['ja']} です。")
            break
        elif lang == '2':
            print(f"\nYour zodiac sign is {seiza1['en']}.")
            break
        else:
            print("1か2を入力してください。")