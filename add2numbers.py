# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        curr1 = l1
        curr2 = l2

        new_list = ListNode(0)
        head = new_list
        
        # while we haven't reached end of both lists 
        while curr1 or curr2:
            new_list.next = ListNode(0)
            new_list = new_list.next
            # if reached end of l1
            if not curr1:
                temp_sum = 0 + curr2.val + carry
                curr2 = curr2.next
            # if reached end of L2
            elif not curr2:
                temp_sum = 0 + curr1.val + carry
                curr1 = curr1.next
            # if we still have both lists
            else:
                temp_sum = curr1.val + curr2.val + carry
                curr1 = curr1.next
                curr2 = curr2.next
            
            new_list.val = temp_sum % 10
            carry = int(temp_sum/10)
      
            
        if carry!=0:
            new_list.next = ListNode(carry)
            new_list = new_list.next     
        
        return head.next
        