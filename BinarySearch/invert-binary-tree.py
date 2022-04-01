from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        tmp_root = root
        stack = [root]
        while stack:
            tmp_left = None
            tmp_right = None
            root = stack.pop()
            if root.left is not None:
                tmp_left = root.left
                stack.append(root.left)
            if root.right is not None:
                tmp_right = root.right
                stack.append(root.right)
            root.left = tmp_right
            root.right = tmp_left
        return tmp_root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

sol = Solution()
a = sol.invertTree(root)
print(a)
