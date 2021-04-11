# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        def inOrder(root, res):
            if not root:
                return
            inOrder(root.left, res) # Traverse left node
            res.append(root.val) # Append current node value to list
            inOrder(root.right, res) # Traverse right node
            return res # Return the appended values list
        array = inOrder(root, [])
        root = cur = TreeNode(array[0])
        for i in range(1, len(array)):
            cur.right = TreeNode(array[i])
            cur = cur.right
        return root