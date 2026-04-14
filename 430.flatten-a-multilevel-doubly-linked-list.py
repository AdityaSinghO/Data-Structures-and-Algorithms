#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
       cur = head
       while cur:
        if cur.child:
            child = cur.child; nxt = cur.next
            cur.next = child; child.prev = cur; cur.child = None
            tail = child
            while tail.next: tail = tail.next
            tail.next = nxt
            if nxt: nxt.prev = tail
        cur = cur.next
       return head
        
# @lc code=end

