"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        result = ListNode(None)
        result_copy = result
        storage = ListNode(None)
        storage_copy = storage
        head_copy = head

        while head_copy:
            if head_copy.val < x:
                result_copy.next = head_copy
                result_copy = result_copy.next
            else:
                storage_copy.next = head_copy
                storage_copy = storage_copy.next
            head_copy = head_copy.next
        storage_copy.next = None
        result_copy.next = storage.next
        return result.next
