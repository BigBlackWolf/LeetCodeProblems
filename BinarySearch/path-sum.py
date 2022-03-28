from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        new_target = targetSum - root.val
        if root.left is None and root.right is None:
            if new_target == 0:
                return True
            return False
        return any((self.hasPathSum(root.left, new_target), self.hasPathSum(root.right, new_target)))


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.right.right.right = TreeNode(1)

root.left.left = TreeNode(11)

root.left.left.right = TreeNode(7)
root.left.left.left = TreeNode(22)

target = 22
sol = Solution()
a = sol.hasPathSum(root, target)
print(a)
