# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMaxPathSum(self, node, result=-sys.maxsize):
 
        # base case: empty tree
        if node is None:
            return 0, result
    
        # find maximum path sum "starting" from the left child
        left, result = self.findMaxPathSum(node.left, result)
    
        # find maximum path sum "starting" from the right child
        right, result = self.findMaxPathSum(node.right, result)
    
        # Try all possible combinations to get the optimal result
        result = max(result, node.val)
        result = max(result, node.val + left)
        result = max(result, node.val + right)
        result = max(result, node.val + left + right)
    
        # return the maximum path sum "starting" from the given node
        return max(node.val, node.val + max(left, right)), result

    def solve(self, root):
        tree, result = self.findMaxPathSum(root)
        return result