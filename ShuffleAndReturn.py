import random

def randomizer(woord):
    woord = ''.join(random.sample(woord, len(woord)))
    print(woord)

randomizer("appel")
randomizer("mediacollege")
randomizer("olifant")