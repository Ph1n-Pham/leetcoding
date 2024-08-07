'''
https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node and a pointer to the curr node
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        # Loop until both lists are exhausted and there's no carry left
        while l1 or l2 or carry:
            # Get the values from the curr nodes or 0 if one of the lists is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and the carry
            math_val = val1 + val2 + carry
            carry = math_val // 10
            add_val = math_val % 10

            # Add the new value to the result list
            curr.next = ListNode(add_val)
            curr = curr.next

            # Move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next


