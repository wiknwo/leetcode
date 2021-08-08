"""Power of Three

    Given an integer n, return true if it is 
    a power of three. Otherwise, return false.

    An integer n is a power of three, if there 
    exists an integer x such that n == 3^x.
    
    Time Complexity: O(log(n))
    Space Complexity: O(1)
"""
class Solution:
    
    def isPowerOfThree(self, n: int) -> bool:
        """Given an integer n, return true if it is a power of three. Otherwise, return false.
        
        Args:
            n(int): Number to check if it's a power of three
            
        Return:
            Boolean indicating if n is a power of three
            
        Raises:
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3;  
        return n == 1;
        
        