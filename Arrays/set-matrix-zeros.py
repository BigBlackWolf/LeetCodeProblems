"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        rows = set()
        cols = set()
        x, y = len(matrix), len(matrix[0])
        for i in range(x):
            for j in range(y):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(x):
            for j in range(y):
                if i in rows or j in cols:
                    matrix[i][j] = 0
 

a = matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(a)
print(a)
