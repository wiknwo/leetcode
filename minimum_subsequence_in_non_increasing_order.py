'''Minimum subsequence in non-increasing order

    William Ikenna-Nwosu (wiknwo)

    Given the array nums, obtain a subsequence of the array 
    whose sum of elements is strictly greater than the sum 
    of the non included elements in such subsequence.     

    If there are multiple solutions, return the subsequence 
    with minimum size and if there still exist multiple 
    solutions, return the subsequence with the maximum total 
    sum of all its elements. A subsequence of an array can 
    be obtained by erasing some (possibly zero) elements 
    from the array. 

    Note that the solution with the given constraints is 
    guaranteed to be unique. Also return the answer sorted 
    in non-increasing order.
'''
from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        min_subsequence_max_total = []
        max_total = -1
        sum_numbers_in_list = sum(nums)
        while sum(min_subsequence_max_total) < sum(nums) or sum(min_subsequence_max_total) > max_total:
            min_subsequence_max_total.append(max(nums))
            nums.remove(max(nums))
            if (sum_numbers_in_list - sum(min_subsequence_max_total)) < sum(min_subsequence_max_total):
                break
        min_subsequence_max_total.sort(reverse = True) # Sort list in descending order
        return min_subsequence_max_total