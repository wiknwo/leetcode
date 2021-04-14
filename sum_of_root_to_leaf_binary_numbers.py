'''Sum of root to leaf binary numbers

    William Ikenna-Nwosu (wiknwo)

    You are given the root of a binary 
    tree where each node has a value 0 
    or 1.  Each root-to-leaf path 
    represents a binary number starting 
    with the most significant bit.  
    For example, if the path is 0 -> 1 -> 
    1 -> 0 -> 1, then this could 
    represent 01101 in binary, which is 
    13.

    For all leaves in the tree, consider 
    the numbers represented by the path 
    from the root to that leaf.

    Return the sum of these numbers. 
    The answer is guaranteed to fit in a 
    32-bits integer.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.runningsum = 0
        self.depth_first_search(root, str(root.val))
        return self.runningsum
    
    def depth_first_search(self, node, binarystring):
        if not node.left and not node.right:
            self.runningsum += int(binarystring, 2) # Convert binary string to integer and add it to running sum
            return 
        if node.left: 
            self.depth_first_search(node.left, binarystring + str(node.left.val))
        if node.right:
            self.depth_first_search(node.right, binarystring + str(node.right.val))