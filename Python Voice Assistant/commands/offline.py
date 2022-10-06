#Dice
from random import randint
def Dice():
    return("I rolled a " + str(randint(1, 6)))

#Coin
def Coin():
    if randint(1, 2) == 1:
        return("It landed on heads!")
    else:
        return("It landed on tails!")
