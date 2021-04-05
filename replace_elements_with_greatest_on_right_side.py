'''Replace elements with greatest on right side

    William Ikenna-Nwosu (wiknwo)

    Given an array arr, replace every element in that array 
    with the greatest element among the elements to its 
    right, and replace the last element with -1.

    After doing so, return the array.
'''
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = 0
        for i in range(len(arr) - 1):
            index = i + 1
            arr[i] = max(arr[index:])
        arr[len(arr) - 1] = -1
        return arr