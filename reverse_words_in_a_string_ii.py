'''Reverse String II

    William Ikenna-Nwosu (wiknwo)

    Given a string s and an integer k, reverse the first k 
    characters for every 2k characters counting from the 
    start of the string.

    If there are fewer than k characters left, reverse all 
    of them. If there are less than 2k but greater than or 
    equal to k characters, then reverse the first k 
    characters and left the other as original.
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index = 0
        characters = [c for c in s]
        # Two pointers 
        while index < len(s):
            left, right = index, min(index + k - 1, len(s) - 1)
            while left < right:
                characters[left], characters[right] = characters[right], characters[left]
                left += 1
                right -= 1
            index += 2 * k
        return ''.join(characters)