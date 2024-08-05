'''
https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150

To determine if a linked list contains a cycle, we can use Floyd's Cycle-Finding Algorithm, also known as the Tortoise and Hare algorithm. 
This algorithm uses two pointers, one moving slowly (the "tortoise") and the other moving quickly (the "hare"). 
If there is a cycle in the list, the hare will eventually meet the tortoise. If the hare reaches the end of the list (i.e., a null pointer), then the list does not contain a cycle.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  # move faster
            
            if slow == fast:
                return True
        
        return False
