'''Make Two Arrays Equal by Reversing Sub-Arrays

    William Ikenna-Nwosu (wiknwo)

    Given two integer arrays of equal length target and arr.

    In one step, you can select any non-empty sub-array of 
    arr and reverse it. You are allowed to make any number 
    of steps.

    Return True if you can make arr equal to target, 
    or False otherwise.
'''
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Check if any number in target is not present in arr
        for number in target:
            if number not in arr:
                return False
        
        # Check that the frequency of numbers in target
        # is equal to the frequency of numbers in arr
        target_dict = {}
        arr_dict = {}
        for number in target:
            if number not in target_dict:
                target_dict[number] = 1
            elif number in target_dict:
                target_dict[number] += 1
        
        for number in arr:
            if number not in arr_dict:
                arr_dict[number] = 1
            elif number in arr_dict:
                arr_dict[number] += 1
            
        if target_dict != arr_dict:
            return False
        
        return True
        
        