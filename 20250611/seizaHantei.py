def seiza(month,day):

    seiza1 = [
        (1, 20, {"ja": "水瓶座", "en": "Aquarius"}),
        (2, 19, {"ja": "魚座", "en": "Pisces"}),
        (3, 21, {"ja": "牡羊座", "en": "Aries"}),
        (4, 20, {"ja": "牡牛座", "en": "Taurus"}),
        (5, 21, {"ja": "双子座", "en": "Gemini"}),
        (6, 22, {"ja": "蟹座", "en": "Cancer"}),
        (7, 23, {"ja": "獅子座", "en": "Leo"}),
        (8, 23, {"ja": "乙女座", "en": "Virgo"}),
        (9, 23, {"ja": "天秤座", "en": "Libra"}),
        (10, 24, {"ja": "蠍座", "en": "Scorpio"}),
        (11, 23, {"ja": "射手座", "en": "Sagittarius"}),
        (12, 22, {"ja": "山羊座", "en": "Capricorn"})
    ]

    for m, d, a in seiza1:
        if(month,day) < (m, d):
            return seiza1[seiza1.index((m,d,a))-1][2]
    return seiza1[-1][2]

