
verzekering_per_maand =  23
benzine_kosten_per_liter =  1.54
liter_per_kilometer = 0.2

invoer = "";

def bereken_maandkosten():
    maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
    print("je maandkosten zijn", maandkosten)

while not isinstance(invoer, float):

    try: 
        km_per_maand = input("hoeveel kilometer rijd jij per maand? ")
        km_per_maand = float(km_per_maand)
        bereken_maandkosten()
        break

    except ValueError:
        print(invoer + " is geen geldig getal")