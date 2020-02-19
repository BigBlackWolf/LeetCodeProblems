"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:

Input: 1->1->1->2->3
Output: 2->3
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
        values = {}
        while head_copy:
            values[head_copy.val] = values.get(head_copy.val, 0) + 1
            head_copy = head_copy.next

        head_copy = head
        while head_copy:
            if values[head_copy.val] == 1:
                result_copy = head_copy
            else:
                result_copy.next = result_copy.next.next
            head_copy = head_copy.next
        return result.next
