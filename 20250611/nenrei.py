#学歴早見
def gakurekiKeisan(nenrei):
    #生年
    seinen = 2025 - nenrei

    print("生年:", seinen)

    #小学
    syougaku = seinen + 1 + 6
    print("小学校:",syougaku,"-",syougaku + 6)
    #中学
    tyugaku = seinen + 1 + 12
    print("中学校:",tyugaku,"-",tyugaku + 3)
    #高校
    koukou = seinen + 1 + 15
    print("高校　:",koukou,"-",koukou + 3)
gakurekiKeisan(19)