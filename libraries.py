import random

# coin = choice(["heads", "tails"])

# print(coin)

#generate random number
# number = random.randint(1, 10)
# print(number)


#shuffle
cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)