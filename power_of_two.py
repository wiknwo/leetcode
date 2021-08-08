import math
"""Power of Two

    Given an integer n, return true if it is 
    a power of two. Otherwise, return false.

    An integer n is a power of two, if there 
    exists an integer x such that n == 2^x.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """Given an integer n, return true if it is a power of two. Otherwise, return false.
        
        Args:
            n(int): Number to check if it's power of two
            
        Return:
            Boolean indicating if n is power of two
            
        Raises:
        """
        if n <= 0: 
            return False
        return math.log2(abs(n)).is_integer()
            
        