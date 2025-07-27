import random
def deck_sample():
    faces = ['Ace', 'Jack', 'Queen', 'King', 'Ace',
             'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten']

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    deck =[(face, suit) for face in faces for suit in suits]

    random.shuffle(deck)

    return deck

def deck_shuffling(deck):
    print("shuffling")
    while len(deck) < 80:
        deck.append(('', ''))

    for index in range(0, 80, 4):
        row = deck[index:index+4]
        print("    ".join(f'{face} of {suit}' if face else '' for face, suit in row))


deck = deck_sample()
deck_shuffling(deck)