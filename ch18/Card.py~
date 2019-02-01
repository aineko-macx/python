import random

class Deck(object):
    

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self, i = 1):
        return self.cards.pop(i)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


    def deal_hands(self, hands, cards):
        handList = [None]*hands
        for i in range(hands):
            handList[i] = Hand('Hand %d' %i)
            self.move_cards(handList[i], cards)
            #print('Hand %d:' %i)
            #print(self.cards)
        return handList

class Card(object):
    """Represents a standard playing card."""


    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank


    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


    def __str__(self):
        return '%s of %s' %(Card.rank_names[self.rank], Card.suit_names[self.suit])


    def __cmp__(self, other):

        #Python 2 only
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        return 0

    def __lt__(self, other):
        #Python 3
        if self.suit > other.suit: return False
        if self.suit < other.suit: return True

        if self.rank > other.rank: return False
        if self.rank < other.rank: return True

class Hand(Deck):
    """Represents a hand of playing cards.
    """

    def __init__(self, label = ''):
        self.cards = []
        self.label = label

    

#card1 = Card(2, 11)
#print(card1)


deck = Deck()


deck.shuffle()

deck.sort()

"""
hand = Hand('new hand')
print(hand.cards)
card = deck.pop_card()
hand.add_card(card)
print(hand)


deck.move_cards(hand, 4)
print(hand)
"""

handList = deck.deal_hands(2,4)
for item in handList:
    print('Hand %d:\n' % handList.index(item), item)
