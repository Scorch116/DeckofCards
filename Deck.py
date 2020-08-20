Importing modules tools
#random - used to select random in the data
# itertools , used to work with iterable in data sets

import random , itertools

#First the deck is made
deck = list(itertools.product(range(1,14),['Heart','Diamond','Club','Spade']))

#Use the random.shuffle to reorganise the order of item in deck
random.shuffle(deck)

print('Your cards....')
for i in range(3): # will print out 3 cards and will display
    print(deck[i][0], 'of', deck[i][1])