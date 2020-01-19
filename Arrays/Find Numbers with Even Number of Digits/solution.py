class Solution:
    def findNumbers(self, nums) -> int:
        counter = 0
        for number in nums:
            if len(str(number)) % 2 == 0:
                counter += 1
        return counter

