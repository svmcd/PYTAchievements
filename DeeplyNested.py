Honger = True
zinInKoken = False
kliekje = False
geld = 9

def goKook() :
    print("Je gaat koken!")

def eetKliekje() :
    print("Je eet een kliekje")

def bestelBroodjeDoner() :
    print("Je bestelt een broodje doner")

def geenHonger() :
    print("Je hebt geen honger")

if Honger == True :
    if zinInKoken == True :
        goKook()
    elif kliekje == True :
        eetKliekje()
    elif geld >= 10 :
        bestelBroodjeDoner()
    else :
        goKook()
else: 
    geenHonger()

