'''Reverse Words in a String III

    William Ikenna-Nwosu (wiknwo)

    Given a string s, reverse the order of characters in 
    each word within a sentence while still preserving 
    whitespace and initial word order.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        tokens = s.split(' ') # Split string into tokens
        
        # Reverse each token
        for i in range(len(tokens)): 
            tokens[i] = tokens[i][::-1]
        
        # Combine tokens into string
        return ' '.join(tokens)