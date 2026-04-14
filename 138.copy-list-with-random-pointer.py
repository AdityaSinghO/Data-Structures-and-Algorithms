#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create a copy of each node and insert it right after the original node
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers for the copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the original list and the copied list
        original_current = head
        copy_head = head.next
        copy_current = copy_head

        while original_current:
            original_current.next = original_current.next.next
            if copy_current.next:
                copy_current.next = copy_current.next.next
            else:
                copy_current.next = None
            
            original_current = original_current.next
            copy_current = copy_current.next

        return copy_head
        
# @lc code=end

