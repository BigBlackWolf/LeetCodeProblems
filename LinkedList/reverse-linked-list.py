"""
Reverse a singly linked list.
Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        result = ListNode(None)
        head_copy = head
        first = True

        while head_copy:
            tmp = head_copy.next
            if first:
                head_copy.next = None
                first = False
                insert = head_copy
            else:
                insert = head_copy
                insert.next = result
            result = insert
            head_copy = tmp
        return result
