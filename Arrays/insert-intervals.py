"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

 """
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = len(intervals)
        result = []
        if newInterval[0] > intervals[-1][0]:
            intervals.append(newInterval)
        
        previous = intervals[0]
        for n in range(1, l):
            if intervals[n][0] > newInterval[0]:
                if newInterval[0] > previous[1]:
                    if newInterval[1] < intervals[n][0]:
                        result.append(previous)
                        current = newInterval
                    elif newInterval[] # ended here
                    



                elif newInterval[1] < previous[0]:
                    result.append(newInterval)
                else:
                    previous = self.merge(previous, newInterval)
            
            if previous[1] >= intervals[n][0]:
                previous = self.merge(previous, intervals[n])
            else:
                result.append(previous)
                previous = intervals[n]
        result.append(previous)
        return result
    
    def merge(self, inter1, inter2):
        start = max(inter1[0], inter2[0])
        end = max(inter1[1], inter2[1])
        return [start, end]
                

a1 = [[1,3],[6,9]], [2,5]
a2 = [[1,3],[6,9]], [4,7]
a3 = [[1,3],[6,9]], [0,5]
a4 = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
res = Solution().insert(*a2)
print(res)