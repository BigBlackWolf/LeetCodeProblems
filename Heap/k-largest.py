"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for n in range(k, len(nums)):
            if nums[n] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[n])
        return heap[0]
        
nums1 = ([3,2,1,5,6,4], 2)
nums2 = ([3,2,3,1,2,4,5,5,6], 4)

res = Solution().findKthLargest(*nums1)
print(res)
