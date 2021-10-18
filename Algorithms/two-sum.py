# https://leetcode.com/problems/two-sum/


from typing import List
import time

nums = [i for i in range(10001)]
target = 19999


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            search_el = target - nums[i]
            if search_el in nums:
                for j in range(len(nums)):
                    if j > i and nums[j] == search_el:
                        return [i, j]
            continue


start = time.time()
a = Solution().twoSum(nums, target)
finish = time.time() - start
print(a, finish)
