"""https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        nums = set(nums)
        while nums:
            item = min(nums)
            nums.remove(item)
            tmp = item
            local_count = 1
            while True:
                tmp += 1
                if tmp in nums:
                    local_count += 1
                    nums.remove(tmp)
                    continue
                break
            if local_count > count:
                count = local_count
        return count


strs = [100,4,200,1,3,2]
test = [i for i in range(-999, 90001)]
test.pop(45000)
sol = Solution().longestConsecutive(test)
print(sol)
