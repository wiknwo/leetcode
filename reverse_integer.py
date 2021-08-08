"""Reverse Integer

    Given a signed 32-bit integer x, return x with 
    its digits reversed. If reversing x causes the 
    value to go outside the signed 32-bit integer 
    range [-231, 231 - 1], then return 0.

    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Where n is number of digits in our input
"""
class Solution:
    # Constants
    MAX_INT = 2**31 - 1 # 2147483647
    MIN_INT = -2**31    # -2147483648
    
    # Instance Methods
    def divider(self, dividend, divisor):
        """Divides dividend by divisor
        
        Args:
            dividend(int): Number to be divided
            divisor(int): Number to divide into dividend
            
        Return:
            
        Raises:
        """
        return int(dividend * 1.0 / divisor)
    
    def modulo(self, dividend, divisor):
        """Performs modulo operation on dividend in way that maintains sign of number
        
        Args:
            dividend(int): Number to be divided
            divisor(int): Number to divide into dividend
        
        Return 
            dividend % divisor
        
        Raises:
        """
        if dividend < 0:
            return dividend % -divisor
        else: 
            return dividend % divisor
        
    def reverse(self, x: int) -> int:
        """Given a signed 32-bit integer x, return x with its digits reversed.
        
        Args: 
            x(int): Number to reverse digits
        
        Return:
            Digits of x reversed
            
        Raises:
        """
        res = 0 # Variable that will contain reversed digits of x
        while x: # Non-zero values in python evaluate to True, while zero evaluates to False
            digit = self.modulo(x, 10)
            x = self.divider(x, 10)
            if res > self.divider(self.MAX_INT, 10) or res == self.divider(self.MAX_INT, 10) and digit > 7:
                return 0
            if res < self.divider(self.MIN_INT, 10) or res == self.divider(self.MIN_INT, 10) and digit < -8:
                return 0
            res = res * 10 + digit
        return res