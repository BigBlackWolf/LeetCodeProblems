class Solution:
    def removeElement(self, nums, val) -> int:
        while nums:
            try:
                index_ = nums.index(val)
                nums.pop(index_)
            except ValueError:
                return len(nums)


arr = [3, 2, 2, 3]
val = 3
a = Solution().removeElement(arr, val)
print(a) # 2
