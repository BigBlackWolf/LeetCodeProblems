# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        l2_list = []
        while l1 is not None:
            value = l1.val if isinstance(l1, ListNode) else l1
            l1_list.append(value)
            l1 = l1.next
        while l2 is not None:
            value = l2.val if isinstance(l2, ListNode) else l2
            l2_list.append(value)
            l2 = l2.next

        result_list = self.mergeArrays(l1_list, l2_list)
        result = ListNode(result_list.pop(-1))
        while result_list:
            tmp = ListNode(result_list.pop(-1))
            tmp.next = result
            result = tmp
        return result

    def mergeArrays(self, arr1, arr2):
        result_list = [x + y for x, y in zip(arr1, arr2)]
        if len(arr1) > len(arr2):
            result_list += arr1[len(arr2):]
        else:
            result_list += arr2[len(arr1):]

        for i in range(len(result_list)):
            if result_list[i] >= 10:
                result_list[i] -= 10
                try:
                    result_list[i + 1] += 1
                except IndexError:
                    result_list.append(1)
        return result_list


test = ListNode(5)
test.next = ListNode(6)
test.next.next = ListNode(0)
test.next.next.next = ListNode(1)

test2 = ListNode(9)

test3 = ListNode(9)
test3.next = ListNode(9)
test3.next.next = ListNode(9)

tests = [(test2, test3), (test, test2), (test, test3)]
sol = Solution()
for i in tests:
    a = sol.addTwoNumbers(*i)
    print(a)
