while True:

    print("半角で数字を入力して(1:三角 2:四角 3:ピラ 4:星 5:六角 6:八角 7:ダイヤ)")
    zukei = input("入力してほしいな、: ") 

    if zukei == "1":
        from sankaku import sankaku
    elif zukei == "2":
        from sikakukei import sikaku
    elif zukei == "3":
        from pyramid import pyra
    elif zukei == "4":
        from hosi import hosi
    elif zukei == "5":
        from seirokukaku import roku
    elif zukei == "6":
        from hati import hati
    elif zukei == "7":
        from daiya import daiya

    yameru = input("もうやめちゃうの？(Yes:y No:n)")
    
    if yameru == "y":
        print("お疲れ様です")
        break
