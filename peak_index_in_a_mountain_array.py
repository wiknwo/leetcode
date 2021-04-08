'''Peak Index in a Mountain Array

    William Ikenna-Nwosu (wiknwo)

    Let's call an array arr a mountain if the 
    following properties hold:

    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... arr[i-1] < arr[i]
        - arr[i] > arr[i+1] > ... > arr[arr.length - 1]

    Given an integer array arr that is guaranteed to be a 
    mountain, return any i such that arr[0] < arr[1] < ... 
    arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
'''
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i