'''Find the Distance Value between Two Arrays

    William Ikenna-Nwosu (wiknwo)

    Given two integer arrays arr1 and arr2, and the integer 
    d, return the distance value between the two arrays.

    The distance value is defined as the number of elements 
    arr1[i] such that there is not any element arr2[j] where 
    |arr1[i]-arr2[j]| <= d.
'''
from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance_value = 0
        count = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) > d:
                    count += 1
            if count == len(arr2):
                distance_value += 1
            count = 0 # Reset count
        return distance_value
        