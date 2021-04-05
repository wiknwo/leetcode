'''Unique Number of Occurrences

    William Ikenna-Nwosu (wiknwo)

    Given an array of integers arr, write a function that 
    returns true if and only if the number of occurrences 
    of each value in the array is unique.
'''
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numberfreq = {}
        for i in range(len(arr)):
            if arr[i] not in numberfreq:
                numberfreq[arr[i]] = 1
            elif arr[i] in numberfreq:
                numberfreq[arr[i]] += 1
        
        return len(numberfreq.values()) == len(set(numberfreq.values()))
                
        