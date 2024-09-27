from umaClasses import Player, cardsAtPlay

def isInt(value):
    if value is None:
        return False
    try:
        int(value)
        return True
    except:
        return False

def getPlayerAmount():
    while True:
        playerAmount = input("How many players are playing (2-8)?: ")
        if not isInt(playerAmount) or not 1 < int(playerAmount) < 9:
            print("Invaild player amount!")
        else: 
            return int(playerAmount)

print(getPlayerAmount())