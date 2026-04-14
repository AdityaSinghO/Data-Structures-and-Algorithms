#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            next_group = tail.next

            curr = prev.next
            prev_node = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = nxt

            group_head = prev.next  
            prev.next = prev_node    
            group_head.next = next_group  

            prev = group_head 
        
# @lc code=end

