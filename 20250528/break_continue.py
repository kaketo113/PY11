#break_continue.py

#break・・・ブレーク・ブレーキ:中断する
#カウンター
count = 1
while(1):
    print("ループ",count)
    count += 1
    #無限ループの止め方:ターミナルクリックしてctlr+c
    nyuuryoku = input("入力してください")
    print("あなたが入力したのは",nyuuryoku,"ですね")
    if nyuuryoku == "助けて" or nyuuryoku == "逃げたい":
        break
    elif nyuuryoku == "戻りたい":
        #continue:続ける（戻る）
        continue
    
    print("処理を続けます")
    print("まだループ中です")
print("ループから脱出")