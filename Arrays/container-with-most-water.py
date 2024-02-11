"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n1 = 0
        n2 = len(height) - 1
        max_val = 0
        while n1 < n2:
            w = n2 - n1
            if height[n1] < height[n2]:
                h = height[n1]
                n1 += 1
            else:
                h = height[n2]
                n2 -= 1
            liters = h * w
            if liters > max_val:
                max_val = liters
        return max_val


a = [1,8,6,2,5,4,8,3,7]
res = Solution().maxArea(a)
print(res)