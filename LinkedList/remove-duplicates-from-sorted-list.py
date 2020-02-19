"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = ListNode(None)
        result.next = head

        result_copy = result
        head_copy = head
        values = set()
        while head_copy:
            if head_copy.val not in values:
                values.add(head_copy.val)
                result_copy = head_copy
            else:
                result_copy.next = result_copy.next.next
            head_copy = head_copy.next
        return result.next
