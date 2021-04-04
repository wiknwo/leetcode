'''Reverse String I

    William Ikenna-Nwosu (wiknwo)

    Write a function that reverses a string. The input 
    string is given as an array of characters s.
'''
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = tmp
            
        