'''Reshape the matrix

    William ikenna-Nwosu (wiknwo)

    In MATLAB, there is a very useful function called 
    'reshape', which can reshape a matrix into a new one 
    with different size but keep its original data. 

    You're given a matrix represented by a two-dimensional 
    array, and two positive integers r and c representing 
    the row number and column number of the wanted reshaped 
    matrix, respectively.

    The reshaped matrix need to be filled with all the 
    elements of the original matrix in the same 
    row-traversing order as they were.

    If the 'reshape' operation with given parameters is 
    possible and legal, output the new reshaped matrix; 
    Otherwise, output the original matrix.
'''
from typing import List
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
            return nums
        
        reshapedmatrix = []
        row = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                row.append(nums[i][j])
                if len(row) == c:
                    reshapedmatrix.append(row)
                    row = []
        return reshapedmatrix