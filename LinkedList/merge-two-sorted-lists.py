"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(None)
        result_copy = result
        l1_copy, l2_copy = l1, l2
        while l1_copy and l2_copy:
            if l1_copy.val < l2_copy.val:
                result_copy.next = l1_copy
                l1_copy = l1_copy.next
            else:
                result_copy.next = l2_copy
                l2_copy = l2_copy.next
            result_copy = result_copy.next
        if l1_copy:
            result_copy.next = l1_copy
        else:
            result_copy.next = l2_copy
        return result.next
