import time
import math

print("Hey, hoe heet je?")
naam = input()
time.sleep(1)
print("Hoi ",naam,", leuke naam! En ik heet Samed.\n")

time.sleep(1)
print("Woon je in Amsterdam, of kom je van ergens anders?\n")
time.sleep(1)

answer1 = input("Amsterdam\nErgens anders\nAntwoord:")

if answer1 == "amsterdam" or answer1 == "Amsterdam" : print("Amsterdam, leuk!")
else: print("Ik ook!") 

time.sleep(1)
print("\nIk kom zelf uit Zaandam.")

time.sleep(1)
print("En hoe oud ben je?")
jij = int(input())
ik = 16

if ik > jij: print("Ik ben 16, ouder dan jij.")
elif ik < jij: print("Jij bent ouder dan ik, ik ben 16.")
elif ik == jij: print("We zijn even oud!")








