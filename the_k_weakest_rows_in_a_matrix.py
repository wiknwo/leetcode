'''The k weakest rows in a matrix

    William Ikenna-Nwosu (wiknwo)

    You are given an m x n binary matrix mat of 1's 
    (representing soldiers) and 0's (representing civilians). 
    The soldiers are positioned in front of the civilians. 
    That is, all the 1's will appear to the left of all the 
    0's in each row.

    A row i is weaker than a row j if one of the following 
    is true:

    - The number of soldiers in row i is less than the 
    number of soldiers in row j.

    - Both rows have the same number of soldiers and i < j.

    Return the indices of the k weakest rows in the matrix 
    ordered from weakest to strongest.
'''
from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        k_weakest_rows = [] # List containing indices of k weakest rows
        soldierfreq = [None] * len(mat) # List mapping row index to soldier count
        num_soldiers = 0 # Varibale to count number of soldiers (1's) in row
        
        # Iterate through matrix
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    num_soldiers += 1 # Count numebr of soldiers in row
            soldierfreq[i] = (i, num_soldiers) # Map row index to soldier frequency
            num_soldiers = 0 # Reset number of soldiers
            
        sorted_soldierfreq = sorted(soldierfreq, key=lambda x: x[1]) # Sort multidimensional list according to frequency
        
        k_weakest_rows = [pair[0] for pair in sorted_soldierfreq[:k]] # Get first k indices in sorted list
        return k_weakest_rows
        