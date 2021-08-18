class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
        Given a roman numeral, convert it to an integer.
        """
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        conversions = {'IV':'IIII', 'IX':'VIIII', 'XL':'XXXX', 'XC':'LXXXX', 'CD':'CCCC', 'CM':'DCCCC' }
        
        for key, value in conversions.items():
            s = s.replace(key, value)
        
        return sum([roman_numerals[char] for char in s])
        