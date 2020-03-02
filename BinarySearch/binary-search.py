"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1



Note:

    You may assume that all elements in nums are unique.
    n will be in the range [1, 10000].
    The value of each element in nums will be in the range [-9999, 9999].
"""


class Solution:
    def search(self, nums, target: int) -> int:
        if nums[0] > target > nums[-1]:
            return -1
        elif nums[0] == target:
            return 0
        start = len(nums) // 2
        last = nums[start]
        while 0 < start < len(nums):
            if target == nums[start]:
                return start
            elif target > nums[start] >= last:
                last = nums[start]
                start += 1
            elif target < nums[start] <= last:
                last = nums[start]
                start -= 1
            else:
                return -1
        return -1
