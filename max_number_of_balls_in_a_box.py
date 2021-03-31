'''Maximum Number of Balls in a box

    William Ikenna-Nwosu (wiknwo)
'''
from typing import List

class Solution:
    def sum_digits(self, n: int) -> int:
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s
    
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box_to_ball_dict = {}
        
        for i in range(lowLimit, highLimit + 1):
            box = self.sum_digits(i)
            if box not in box_to_ball_dict:
                box_to_ball_dict[box] = 1
            elif box in box_to_ball_dict:
                box_to_ball_dict[box] += 1
        
        return max(box_to_ball_dict.values())
    
    
                