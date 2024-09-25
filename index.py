import math
import random

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "S", "R", "+2", "W"]*4 + [1, 2, 3, 4, 5, 6, 7, 8, 9, "S", "R", "+2", "+4"]*4 # 0-55 first chunk, 56-end is rest
cardsAtPlay = []

class Card:
    def __init__(self, cardId):
        self.cardId = cardId
        self.symbol = str(deck[cardId])
        self.color = self.getColor()

    def getColor(self):
        if deck[self.cardId] in ["+4", "W"]: return "wild"
        elif self.cardId <= 55:
            if math.ceil((self.cardId+1)/14) == 1: return "red"
            elif math.ceil((self.cardId+1)/14) == 2: return "yellow"
            elif math.ceil((self.cardId+1)/14) == 3: return "green"
            elif math.ceil((self.cardId+1)/14) == 4: return "blue"
        elif self.cardId >= 56:
            if math.ceil((self.cardId-55+1)/13) == 1: return "red"
            elif math.ceil((self.cardId-55+1)/13) == 2: return "yellow"
            elif math.ceil((self.cardId-55+1)/13) == 3: return "green"
            elif math.ceil((self.cardId-55+1)/13) == 4: return "blue"

    def toJSON(self):
        return self.__dict__

randomCard = random.randint(0, len(deck)-1)
cardsAtPlay += [randomCard]

print(Card(randomCard).toJSON())
print(cardsAtPlay)