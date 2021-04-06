'''X of a kind in a deck of cards

    William Ikenna-Nwosu (wiknwo)

    In a deck of cards, each card has an integer written 
    on it.

    Return true if and only if you can choose X >= 2 such 
    that it is possible to split the entire deck into 1 or 
    more groups of cards, where:

    - Each group has exactly X cards.
    - All the cards in each group have the same integer. 
'''
from typing import List

class Solution:
    def gcd(self, x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        cardfreq = {}
        
        # Calculating card frequencies
        for i in range(len(deck)):
            if deck[i] not in cardfreq:
                cardfreq[deck[i]] = 1
            elif deck[i] in cardfreq:
                cardfreq[deck[i]] += 1
        
        # Determine if frequencies are multiples of each other
        frequencies = list(cardfreq.values())
        for i in range(len(frequencies) - 1):
            if frequencies[i] >= 2: 
                if self.gcd(frequencies[i], frequencies[i + 1]) == 1:
                    return False
        return True
            
            