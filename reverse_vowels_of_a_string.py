'''Reverse Vowels of a String

    William Ikenna-Nwosu (wiknwo)

    Given a string s, reverse only all the vowels in the 
    string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they 
    can appear in both cases.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        vowelcount = 0
        stringlist = list(s) # Converting string to list
        
        
        # Getting order of appearance of vowels
        for i in range(len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                vowels.append(s[i])
        
        # Placing vowels back into string in reverse order
        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                stringlist[i] = vowels[vowelcount]
                vowelcount += 1
        return ''.join(stringlist)
        