"""Power of Four

    Given an integer n, return true if it is 
    a power of four. Otherwise, return false.

    An integer n is a power of four, if there 
    exists an integer x such that n == 4^x.
    
    Time Complexity: O(log(n))
    Space Complexity: O(1)
"""
class Solution:
    
    def isPowerOfFour(self, n: int) -> bool:
        """Given an integer n, return true if it is a power of four. Otherwise, return false.
        
        Args:
            n(int): Number to check if it's a power of four
            
        Return:
            Boolean indicating if n is a power of four
            
        Raises:
        """
        if n <= 0:
            return False
        while n % 4 == 0:
            n /= 4;  
        return n == 1;
        
        