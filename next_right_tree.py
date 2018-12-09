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
        """connects the next of each node to its right node"""
        
        if not root:
            return root
        
        root.next = None
        curr = root
            
        self.h_connect(curr)
        # print(root.next)
        # print(root.left.next.val)
        return root
        
        
    def h_connect(self, curr):
        """helper function to recursively call the tree in DFS"""

        if curr.next:
            if curr.right:
                curr.right.next = curr.next.left
                # curr.next.left.next = curr.next.right
            else:
                return
        if curr.left:
            curr.left.next = curr.right
            self.h_connect(curr.left)
            self.h_connect(curr.right)
            
tree = TreeLinkNode(10)   
tree.left = TreeLinkNode(5)   
tree.right = TreeLinkNode(15)   
solution1 = Solution()
solution1.connect(tree)