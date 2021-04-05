'''Available Captures for Rook

    William Ikenna-Nwosu (wiknwo)

    On an 8 x 8 chessboard, there is exactly one white rook 
    'R' and some number of white bishops 'B', black pawns 
    'p', and empty squares '.'.

    When the rook moves, it chooses one of four cardinal 
    directions (north, east, south, or west), then moves in 
    that direction until it chooses to stop, reaches the 
    edge of the board, captures a black pawn, or is blocked 
    by a white bishop. A rook is considered attacking a 
    pawn if the rook can capture the pawn on the rook's 
    turn. The number of available captures for the white 
    rook is the number of pawns that the rook is 
    attacking.

    Return the number of available captures for the white 
    rook.
'''
from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_index_i = -1
        rook_index_j = -1
        available_captures = 0
        for i in range(len(board)):
            for j in range(i, len(board[i])):
                if board[i][j] == 'R':
                    rook_index_i = i
                    rook_index_j = j
        
        # Find pawns in x-direction forward
        for i in range(rook_index_i, len(board)):
            if board[rook_index_i][i] == 'p':
                available_captures += 1
                break
            
            if board[rook_index_i][i] == 'B':
                break
                
        # find pawns in x-direction backward
        for i in range(rook_index_i, -1, -1):
            if board[rook_index_i][i] == 'p':
                available_captures += 1
                break
                
            if board[rook_index_i][i] == 'B':
                break
        
        # Find pawns in y-direction down
        for j in range(rook_index_j, len(board)):
            if board[j][rook_index_j] == 'p':
                available_captures += 1
                break
                
            if board[j][rook_index_j] == 'B':
                break
        
        # Find pawns in y-direction up
        for j in range(rook_index_j, -1, -1):
            if board[j][rook_index_j] == 'p':
                available_captures += 1
                break
                
            if board[j][rook_index_j] == 'B':
                break
                
        return available_captures
        