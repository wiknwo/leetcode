'''N-ary Tree Preorder Traversal

    William Ikenna-Nwosu (wiknwo)

    Given the root of an n-ary tree, return the preorder 
    traversal of its nodes' values.

    Nary-Tree input serialization is represented in their 
    level order traversal. Each group of children is 
    separated by the null value (See examples)
'''
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = []
        for child in root.children:
            result.extend(self.preorder(child))
            
        return [root.val] + result