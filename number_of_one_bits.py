"""Number of 1 Bits

    Write a function that takes an unsigned integer 
    and returns the number of '1' bits it has (also 
    known as the Hamming weight).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Where n is the size of the input
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        """Count number of ones in bit representation of n
        
        Args:
            n(int): Number to count number of ones of
            
        Return:
            Number of ones in bit representation of n
        
        Raises
        """
        return bin(n).count("1")