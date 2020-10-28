import time

print("Je bent bijna te laat voor school en gaat de deur uit onderweg naar het station. Je ziet dat je fietsband lek is, ga je weer terug om je fietsband te pompen of ga je lopend naar het station?\n\nPOMPEN\nLOPEN\n")
keuze = input()
if keuze == 'POMPEN':
    print("Je pompt je fietsband en je komt op tijd")
elif keuze == 'LOPEN':
    print("Je gaat lopend naar het station en komt op tijd")
else:
    print("error")


time.sleep(2)
print("\n\nJe stapt in de trein en ziet dat het best druk is. Ga je staan of zoeken naar een plek om te zitten?\n\nSTAAN\nZOEKEN\n")
keuze = input()
if keuze == 'STAAN':
    print("Je blijft staan")
elif keuze == 'ZOEKEN':
    print("Je zoekt naar een plek om te zitten en je vindt er een")
else:
    print("error")


time.sleep(2)
print("\n\nJe stapt uit de trein en je hebt nog weinig tijd. Je ziet dat iemand zijn/haar portemonnee heeft laten vallen, pak je de portemonnee en breng je het terug of loop je door?\n\nTERUG\nDOORLOPEN\n")
keuze = input()
if keuze == 'TERUG':
    print("Je brengt het terug en de persoon geeft je 5 euro als dank")
elif keuze == 'DOORLOPEN':
    print("Je loopt door")
else:
    print("error")


time.sleep(2)
print("\n\nJe bent onderweg naar school en krijgt honger, ga je tussendoor snel naar de Albert Heijn of wacht je tot je pauze.\n\nAH\nPAUZE\n")
keuze = input()
if keuze == 'AH':
    print("Je haalt een croissant en komt precies op tijd")
elif keuze == 'PAUZE':
    print("Je gaat in de pauze naar Albert Heijn")
else:
    print("error")


time.sleep(2)
print("\n\nJe bent op school en er wordt belangrijke lesstof uitgelegd, ga je bij je vrienden zitten of ergens anders waar het rustig is?\n\nVRIENDEN\nANDERS\n")
keuze = input()
if keuze == 'VRIENDEN':
    print("Je zit met je vrienden, het is leuk maar je begrijpt weinig van de lesstof")
elif keuze == 'ANDERS':
    print("Je luistert goed en begrijpt alles")
else:
    print("error")