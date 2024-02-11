"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
"""

from typing import List

class Solution:
    # Working but not optimal
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     n = len(numbers)
    #     for i in range(n):
    #         wanted = target - numbers[i]
    #         if wanted in numbers[i + 1:]:
    #             return [i + 1, numbers[i+1:].index(wanted) + 1 + i + 1]
    #     return [-1, -1]
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n1 = 0
        n2 = len(numbers) - 1
        while n1 < n2:
            value = numbers[n1] + numbers[n2]
            if value == target:
                return [n1 + 1, n2 + 1]
            elif value > target:
                n2 -= 1
            elif value < target:
                n1 += 1
        return [-1, -1]



a = [2,7,11,15,17]
target = 22
res = Solution().twoSum(a, target)
print(res)