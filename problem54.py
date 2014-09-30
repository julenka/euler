#!/usr/bin/env python

__author__='Julia Schwarz'

'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace. (T is 10)

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

from collections import defaultdict

value_map = {'2': 0, '3':1, '4': 2, '5':3, '6':4, '7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}

class Hand:
    def __init__(self, cards):
        '''
        cards: ['2C','5C','8X','8D','TD']
        '''
        self.suit_to_values = defaultdict(list)
        self.values_to_suit = defaultdict(list)
        self.values = []
        for v,s in cards:
            self.suit_to_values[s].append(value_map[v])
            self.values_to_suit[value_map[v]].append(s)
            self.values.append(value_map[v])

    def compareValues(self, other):
        '''
        return 1 if me > other, -1 if other > me, 0 otherwise
        '''
        print "++++++COMPARE++++++++"
        my_values_sorted = reversed(sorted(self.values))
        other_values_sorted = reversed(sorted(other.values))
        for (my_val, other_val) in zip(my_values_sorted, other_values_sorted):
            if(my_val > other_val):
                return 1
            if(other_val > my_val):
                return -1
        return 0

    def compareTo(self, other):
        '''
        return 1 if me > other, -1 if other > me, 0 otherwise
        '''
        my_rank, my_value = self.getRank()
        other_rank, other_value = other.getRank()
        if(my_rank > other_rank):
            return 1
        if(my_rank < other_rank):
            return -1
        if(my_value > other_value):
            return 1
        if(my_value < other_value):
            return -1
        return self.compareValues(other)

    def getRank(self):
        ''' Returns the rank of hand in form (rank, value)
        0: High Card
        1: One Pair
        2: Two Paris
        3: Three of a Kind
        4: Straight
        5: Flush
        6: Full House
        7: Four of a Kind
        8: Straight Flush
        9: Royal Flush
        '''
        royals = set(['T','J','Q','K','A'])
        for suit,values in self.suit_to_values.iteritems():
            if len(values) == 5:
                # Check royal flush
                if(set(values) == royals):
                    # 9 is rank of royal flush, 12 is value of highest card in hadn
                    return (9, 12)
                # Check straight flush
                if(max(values) - min(values) == 4):
                    return (8, max(values))
                # return flush
                return (5, max(values))
        for value, suits in self.values_to_suit.iteritems():
            if len(suits) == 4:
                # four of a kind
                return (7, value)
            # check 3 of a kind
            if len(suits) == 3:
                if len(self.values_to_suit) == 2:
                    # full house
                    return (6, max(self.values_to_suit.keys()))
                else:
                    # 3 of a kind
                    return (3, value)
            if len(suits) == 2:
                # 2 pair
                if(len(self.values_to_suit.keys()) == 3):
                    othervalue = 0
                    for value2, suits2 in self.values_to_suit.iteritems():
                        if len(suits2) == 2:
                            othervalue = value2
                    return (2, max(value, othervalue))
                # one pair
                else:
                    return (1, value)

        # check straight
        if (max(self.values) - min(self.values) == 4):
            return (4, max(self.values))

        # high card
        return (0, max(self.values))


poker_hands = open('p054_poker.txt').readlines()

p1_count = 0
print "p1\tp2\twinner"
for line in poker_hands:
    cards = line.strip().split(' ')
    p1_hand = Hand(cards[:5])
    p2_hand = Hand(cards[5:])
    result = p1_hand.compareTo(p2_hand)
    if(result > 0):
        p1_count += 1
        winner = "p1"
    elif result < 0:
        winner = "p2"
    else:
        winner = "tie"
    print repr(cards[:5]), "\t", repr(cards[5:]), "\t", winner, p1_hand.getRank(), p2_hand.getRank()

print p1_count
