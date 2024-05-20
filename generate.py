import random 

coin = random.choice(["heads" , "tails"])# Verilen listeden eleman seçer.
print(coin)

"""
from random import choice

coin = choice(["heads", "tails"])
print(coin)
                      2 Durum da aynı sonucu verir.
"""

number = random.randint(1,10) # Verilen aralıkta random bir int değeri seçer
print(number)

cards = ["Jack", "Queen", "King","As"]
random.shuffle(cards) # Verilen listeyi karıştıran bir komut
for card in cards: # Kartları teker teker yazılması için
    print(card)