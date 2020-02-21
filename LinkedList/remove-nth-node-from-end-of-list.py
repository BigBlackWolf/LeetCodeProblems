"""
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next and n == 1:
            return None
        last_nodes = [None] * (n + 1)
        head_copy = head
        counter = 0

        while head_copy:
            last_nodes[counter % (n + 1)] = head_copy
            if not head_copy.next:
                if n == 1:
                    last_nodes[(counter + 1) % (n + 1)].next = None
                elif n <= counter:
                    last_nodes[(counter + 1) % (n + 1)].next = last_nodes[(counter + 3) % (n + 1)]
                else:
                    head = last_nodes[0].next
            counter += 1
            head_copy = head_copy.next
        return head
