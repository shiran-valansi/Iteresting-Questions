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

##########################################################################
###################        ITERATIVE SOLUTION           ##################

# class Solution:
#     def preorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         preorder = []
#         stack = []
        
#         if not root:
#             return preorder
#         stack.append(root)
#         while stack:
#             curr = stack.pop()
#             preorder.append(curr.val)
#             if curr.right:
#                 stack.append(curr.right)
#             if curr.left:
#                 stack.append(curr.left)

#         return preorder