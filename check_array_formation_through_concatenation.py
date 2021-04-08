'''Check Array Formation Through Concatenation

    William Ikenna-Nwosu (wiknwo)

    You are given an array of distinct integers arr and an 
    array of integer arrays pieces, where the integers in 
    pieces are distinct. Your goal is to form arr by 
    concatenating the arrays in pieces in any order. 
    However, you are not allowed to reorder the integers in 
    each array pieces[i].

    Return true if it is possible to form the array arr 
    from pieces. Otherwise, return false.
'''
from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index_value_pairs = []
        for i in range(len(pieces)):
            for j in range(len(pieces[i])):
                if pieces[i][j] not in arr:
                    return False
            piece_index = arr.index(pieces[i][0]) # index of piece is the index of first part of piece
            index_value_pairs.append((piece_index, pieces[i])) # Store index of piece and piece as tuple in list
            sorted_index_value_pairs = sorted(index_value_pairs, key=lambda x: x[0]) # Sort pieces according to index
            
        # Concatenate pieces
        concatenated_list = []
        for i in range(len(sorted_index_value_pairs)):
            for element in sorted_index_value_pairs[i][1]:
                concatenated_list.append(element)

        return concatenated_list == arr
       
            
            