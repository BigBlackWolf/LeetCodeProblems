"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        
        output = []
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                value = matrix[top][col]
                output.append(value)
            top += 1

            for row in range(top, bottom + 1):
                value = matrix[row][right]
                output.append(value)
            right -= 1
            
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    value = matrix[bottom][col]
                    output.append(value)
                bottom -= 1
            
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    value = matrix[row][left]
                    output.append(value)
                left += 1

        return output


a = [[1, 2, 3], [4,5,6], [7,8,9]]
# a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
# a = [[1, 2, 11],[3, 4, 12],[5, 6,13],[7, 8,14],[9, 10,15]]
res = Solution().spiralOrder(a)
print(res)
