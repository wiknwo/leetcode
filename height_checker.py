'''Height Checker

    William Ikenna-Nwosu (wiknwo)

    Students are asked to stand in non-decreasing order of 
    heights for an annual photo.

    Return the minimum number of students that must move in 
    order for all students to be standing in non-decreasing 
    order of height.

    Notice that when a group of students is selected they 
    can reorder in any possible way between themselves and 
    the non selected students remain on their seats.
'''
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        inversions = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                inversions += 1
        return inversions