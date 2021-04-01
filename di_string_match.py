'''DI String Match

    William Ikenna-Nwosu (wiknwo)

    Given a string S that only contains "I" (increase) or 
    "D" (decrease), let N = S.length.

    Return any permutation A of [0, 1, ..., N] such that for 
    all i = 0, ..., N-1:

    If S[i] == "I", then A[i] < A[i+1]
    If S[i] == "D", then A[i] > A[i+1]
'''
from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        sequence = []
        low, high = 0, len(S)
        
        for i in range(len(S)):
            if S[i] == 'I':
                sequence.append(low)
                low += 1
            if S[i] == 'D':
                sequence.append(high)
                high -= 1
        sequence.append(low)
        return sequence
        