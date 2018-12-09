# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder = []
        self.helper(root, inorder)
        return inorder
        
        
    def helper(self, root, inorder):
        if root == None:
            return 
        if root.left != None:
            self.helper(root.left,inorder)
        inorder.append(root.val)
        if root.right != None:
            self.helper(root.right,inorder)