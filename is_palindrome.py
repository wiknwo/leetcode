class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Return boolean indicating if number is a palindrome
        """
        number = str(x)
        for i in range(len(number) // 2):
            if number[i] != number[len(number) - 1 - i]:
                return False
        return True
        