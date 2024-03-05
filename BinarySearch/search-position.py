"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] < target:
                r = mid - 1
            else:
                return mid
        return l



nums1 = ([1,3,5,6], 5)
nums2 = ([1,3,5,6], 2)
nums3 = ([1,3], 3)
nums4 = ([1,3, 5], 5)
nums5 = ([2,7, 8, 9, 10], 9)
nums6 = ([1,3, 5, 6], 2)

res = Solution().searchInsert(*nums6)
print(res)
