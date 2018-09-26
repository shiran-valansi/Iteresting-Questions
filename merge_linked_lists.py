# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
    
        # curr1 = l1
        # curr2 = l2
        l3 = ListNode('')
        curr3 = l3
        # while we haven't reached the ends of either lists
        while l1 and l2:
            # find out which node has the greater value and put in new list
            if l1.val < l2.val:
                curr3.val = l1.val
                l1 = l1.next
            else:
                curr3.val = l2.val
                l2 = l2.next
            curr3.next = ListNode(None)
            curr3 = curr3.next
        # if we've reached the end of either list, find out which list that was and continue to add nodes from the longer list
        if l1:
            curr3.val = l1.val
            curr3.next = l1.next
        elif l2:
            curr3.val = l2.val
            curr3.next = l2.next
            
        
        return l3
            