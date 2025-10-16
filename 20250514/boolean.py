yakinikuSuki = True # True(Yes) / false(No)
susiSuki = True
currySuki = False

if (yakinikuSuki and susiSuki or yakinikuSuki and currySuki or currySuki and susiSuki)\
      and not (yakinikuSuki and susiSuki and currySuki):
    print("めんどくさい人ですね")