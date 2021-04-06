'''Squares of a Sorted Array

    William Ikenna-Nwosu (wiknwo)

    Given an integer array nums sorted in non-decreasing 
    order, return an array of the squares of each number 
    sorted in non-decreasing order.
'''
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squarednums = [num * num for num in nums]
        return sorted(squarednums)
        