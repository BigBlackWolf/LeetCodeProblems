"""
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
        elements = set(nums)
        sequence = 0
        
        for n in elements:
            if (n - 1) not in elements:
                tmp_seq = 1
                while n + tmp_seq in elements:
                    tmp_seq += 1
                sequence = max(tmp_seq, sequence)
        return sequence

a1 = [100,4,200,1,3,2] # 4
a2 = [0,3,7,2,5,8,4,6,0,1] # 9
a3 = [0, 0] # 1
a4 = [0] # 1
a5 = [] # 0
a6 = [0,3,7,2,8, 9, 10, 11,4,6,0,1] # 5

res = Solution().longestConsecutive(a6)
print(res)

            
            
        