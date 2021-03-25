'''Set Mismatch

    William Ikenna-Nwosu (wiknwo)

    You have a set of integers s, which originally contains 
    all the numbers from 1 to n. Unfortunately, due to some 
    error, one of the numbers in s got duplicated to another 
    number in the set, which results in repetition of one 
    number and loss of another number.

    You are given an integer array nums representing the 
    data status of this set after the error.

    Find the number that occurs twice and the number that is 
    missing and return them in the form of an array.
'''
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numbers = {}
        
        # Count frequencies of numbers
        for i in range(len(nums)):
            if nums[i] not in numbers:
                numbers[nums[i]] = 1
            if nums[i] in numbers:
                numbers[nums[i]] += 1
        
        # Find missing value
        missing_value = -1
        for i in range(len(nums)):
            if (i + 1) not in numbers.keys():
                missing_value = i + 1
                break
        
        return [max(numbers, key=numbers.get), missing_value]