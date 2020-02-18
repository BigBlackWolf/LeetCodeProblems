"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        head_copy = head
        while head_copy:
            if head_copy.next and head_copy.next.val == val:
                if not head_copy.next:
                    del head_copy
                    break
                else:
                    head_copy.next = head_copy.next.next
            else:
                head_copy = head_copy.next
        return head
