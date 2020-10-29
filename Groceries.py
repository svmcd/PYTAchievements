
groceryList = ["appels" , "melk" , "eieren" , "brood" , "boter" , "pindakaas"]
shoppingCart = ["appels" , "melk" , "eieren" , "brood" , "boter"]


for x in groceryList:
    print(x)
print("\n")

for x in shoppingCart:
    print(x)
print("\n")


if groceryList == shoppingCart:
    print("done shopping!")
else: 
    print("continue shopping")