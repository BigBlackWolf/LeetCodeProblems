""" https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

 3
9  20
  15 7

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""
from typing import List, Optional
from memory_profiler import profile


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def rucursion(preorder, inorder):
            if len(preorder) == 0:
                return None
            root = TreeNode(preorder[0])
            in_index = inorder.index(preorder[0])
            root.left = rucursion(preorder[1:in_index + 1], inorder[:in_index])
            root.right = rucursion(preorder[in_index + 1:], inorder[in_index + 1:])
            return root

        root_main = TreeNode(preorder[0])
        in_index = inorder.index(preorder[0])
        root_main.left = rucursion(preorder[1:in_index + 1], inorder[:in_index])
        root_main.right = rucursion(preorder[in_index + 1:], inorder[in_index + 1:])
        return root_main


preorder = [i for i in range(700)]
inorder = [i for i in range(700)]
sol = Solution().buildTree(preorder, inorder)

