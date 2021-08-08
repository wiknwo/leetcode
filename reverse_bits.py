"""Reverse Bits

    Reverse bits of a given 32 bits unsigned integer.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        """Reverse bits of a given 32 bits unsigned integer.
        
        Args:
            n(int): Bit sting to be reversed
            
        Return:
            Bit string reversed
            
        Raises:
        """
        res = 0
        for i in range(32):
            if (n >> i) & 1:
                res += ((n >> i) & 1) << (31 - i)
        return res