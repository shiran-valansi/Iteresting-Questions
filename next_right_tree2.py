# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        self.helper(root)
        
        
    def helper(self, root):
        
        if not root:
            return
        if root.next:
            if root.right:
                root.right.next = self.find_next(root.next, True)
        if root.left:
            root.left.next = self.find_next(root, False)
        self.helper(root.left)
        self.helper(root.right)
        
    def find_next(self, root, check_both):
        """ finds the next pointer """
        
        if root == None:
            return None
            
        if check_both:
            if root.left:
                return root.left
        if root.right:
                return root.right
        return self.find_next(root.next, True)
tree = TreeLinkNode(10)   
tree.left = TreeLinkNode(5)   
tree.right = TreeLinkNode(15)   
solution1 = Solution()
solution1.connect(tree)
