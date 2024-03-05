"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if not intervals:
            return result
        
        intervals.sort(key=lambda x: x[0])
        current = intervals[0]
        for i in range(1, len(intervals)):
            processing = intervals[i]
            if processing[0] <= current[1]:
                current[1] = max(processing[1], current[1])
            else:
                result.append(current)
                current = processing
        result.append(current)
        return result

a1 = [[4,5], [1,4]]
a2 = [[1,3],[2,6],[8,10],[15,18]]
a3 = []
a4 = [[1,2], [3, 4], [1, 5], [2, 7]]
res = Solution().merge(a4)
print(res)