# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder = []
        if not root:
            return preorder
        self.helper(root, preorder)
        return preorder
    
    def helper(self, root, preorder):
        preorder.append(root.val)
        if root.left:
            self.helper(root.left,preorder)
        if root.right:
            self.helper(root.right, preorder)