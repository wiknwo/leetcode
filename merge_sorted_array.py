'''Merge sorted array

    William Ikenna-Nwosu (wiknwo)

    Given two sorted integer arrays nums1 and nums2, 
    merge nums2 into nums1 as one sorted array.

    The number of elements initialized in nums1 and nums2 
    are m and n respectively. You may assume that nums1 has 
    a size equal to m + n such that it has enough space to 
    hold additional elements from nums2.

    Input: nums1 = [1,2,3,0,0,0], m = 3, 
           nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
'''
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right, i, j = m + n - 1, m - 1, n - 1
        
        # Traverse both lists
        while i >= 0 and j >= 0:
            # Check if current element of first list
            # is smaller than current element of
            # second list. If yes, store first list
            # element and increment first list index.
            # Otherwise do same with second list
            if nums1[i] > nums2[j]:
                nums1[right] = nums1[i]
                i, right = i - 1, right - 1
            else:
                nums1[right] = nums2[j]
                j, right = j - 1, right - 1
        
        # Store remaining elements of second list
        while j >= 0:
            nums1[right] = nums2[j]
            j, right = j - 1, right - 1