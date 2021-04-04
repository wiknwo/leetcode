'''Hamming Distance

    William Ikenna-Nwosu (wiknwo)

    The Hamming distance between two integers is the number 
    of positions at which the corresponding bits are 
    different.

    Given two integers x and y, calculate the Hamming distance.
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x_bin = bin(x)[2:].zfill(32)
        y_bin = bin(y)[2:].zfill(32)
        
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                count += 1
        return count