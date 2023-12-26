# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
     
        # base condition when binary tree is empty
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
 
    # function to check if tree is height-balanced or not
    def isBalanced(self, root):
        
        # Base condition
        if root is None:
            return True
    
        # for left and right subtree height
        lh = self.height(root.left)
        rh = self.height(root.right)
    
        # allowed values for (lh - rh) are 1, -1, 0
        if (abs(lh - rh) <= 1) and self.isBalanced(
        root.left) is True and self.isBalanced(root.right) is True:
            return True
    
        # if we reach here means tree is not
        # height-balanced tree
        return False
    

    def solve(self, root):
        return self.isBalanced(root)