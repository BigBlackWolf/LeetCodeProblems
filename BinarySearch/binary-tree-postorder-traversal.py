from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
            result.insert(0, root.val)
        return result


root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(2)

sol = Solution()
a = sol.postorderTraversal(root)
print(a)
