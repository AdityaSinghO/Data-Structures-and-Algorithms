#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        # Find the length of the list and the tail node
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        # Connect the tail to the head to make it circular
        tail.next = head
        # Find the new tail:
        new_tail = head
        for _ in range(length - k % length - 1):
            new_tail = new_tail.next
        # The new head is the next node after the new tail
        new_head = new_tail.next
        # Break the circle
        new_tail.next = None
        return new_head
    
        
# @lc code=end

