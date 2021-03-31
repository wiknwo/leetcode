'''1-bit and 2-bit characters

    William Ikenna-Nwosu (wiknwo)

    We have two special characters. The first character can 
    be represented by one bit 0. The second character can be 
    represented by two bits (10 or 11).

    Now given a string represented by several bits. 
    Return whether the last character must be a one-bit 
    character or not. The given string will always end 
    with a zero.
'''
from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits) - 1
        count = 0
        while count < n:
            count += bits[count] + 1
        return count == n

# You start reading from left to right, if you encounter 
# bits[i] == 0, it means that the next character will have 
# 1 bit. And if bits[i] == 1 it means that the next character 
# will have 2 bits. You keep incrementing the count to the 
# start of each next character. In the end, if count is 
# equals to n, it would mean that the last character is 
# 1 bit.