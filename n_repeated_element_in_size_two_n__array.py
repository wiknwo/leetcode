'''N Repeated Element in Size 2N Array

    William Ikenna-Nwosu (wiknwo)

    In a array A of size 2N, there are N+1 unique 
    elements, and exactly one of these elements is 
    repeated N times.

    Return the element repeated N times.
'''
from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        numbercount = {}
        for i in range(len(A)):
            if A[i] not in numbercount:
                numbercount[A[i]] = 1
            if A[i] in numbercount:
                numbercount[A[i]] += 1
        return max(numbercount, key=numbercount.get)