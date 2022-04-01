from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return result


root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
a = sol.preorderTraversal(root)
print(a)
