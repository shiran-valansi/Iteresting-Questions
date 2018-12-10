class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # take the max between left and right trees plus 1
        
        depth = max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1) 
        return depth