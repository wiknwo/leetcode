'''Sum of Unique elements

    William Ikenna-Nwosu (wiknwo)

    You are given an integer array nums. The unique elements 
    of an array are the elements that appear exactly once in 
    the array.

    Return the sum of all the unique elements of nums.
'''
from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        numberfreq = {}
        for i in range(len(nums)):
            if nums[i] not in numberfreq:
                numberfreq[nums[i]] = 1
            elif nums[i] in numberfreq:
                numberfreq[nums[i]] += 1
        
        runningsum = 0
        for key in numberfreq.keys():
            if numberfreq[key] == 1:
                runningsum += key
        
        return runningsum
                
        