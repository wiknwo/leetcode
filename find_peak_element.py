'''Find Peak Element

    William Ikenna-Nwosu (wikwno)

    A peak element is an element that is strictly greater 
    than its neighbors.

    Given an integer array nums, find a peak element, and 
    return its index. If the array contains multiple peaks, 
    return the index to any of the peaks.

    You may imagine that nums[-1] = nums[n] = -∞.
'''
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num = nums[0]
        peak_index = 0
        
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
        for i in range(1, len(nums) - 1):
            if nums[i - i] < nums[i] and nums[i] > nums[i + 1] and nums[i] > max_num:
                peak_index = i
                max_num = nums[i]
    
        if nums[len(nums) - 1] > max_num:
            return len(nums) - 1
        
        return peak_index
        