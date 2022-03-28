from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 0:
            return None
        root = len(nums) // 2
        tree = TreeNode(nums[root])

        tree.left = self.sortedArrayToBST(nums[:root])
        tree.right = self.sortedArrayToBST(nums[root + 1:])
        return tree


nums = [-10, -3, 0, 5, 9]
sol = Solution()
a = sol.sortedArrayToBST(nums)
print(a)
