"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        result = ListNode(None)
        result_copy = result
        head_copy = head
        counter = 0

        while head_copy:
            counter += 1
            if counter % 2 != 0:
                if head_copy.next and head_copy.next.next:
                    second = head_copy.next
                    third = head_copy.next.next
                    head_copy.next = third
                    second.next = head_copy
                    result_copy.next = second
                    head_copy = second
                elif head_copy.next and head_copy.next.next is None:
                    second = head_copy.next
                    head_copy.next = None
                    second.next = head_copy
                    result_copy.next = second
            result_copy = result_copy.next
            head_copy = head_copy.next
        return result.next

