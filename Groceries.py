
lijst1 = ["appels" , "melk" , "eieren" , "brood" , "boter" , "pindakaas"]
lijst2 = ["appels" , "melk" , "eieren" , "brood" , "boter"]


print("\n")

print("grocery list:")

for x in lijst1:
    print(x)

print("\n")

print("shopping cart:")

for x in lijst2:
    print(x)

print("\n")

if lijst1 == lijst2:
    print("done shopping!")

else: 
    print("continue shopping")