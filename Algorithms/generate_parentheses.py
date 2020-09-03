"""
https://leetcode.com/problems/generate-parentheses/

 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

from itertools import product


class Solution:
    def generateParenthesis(self, n: int):
        array = ["(", ")"]
        variants = product(array, repeat=n*2)
        opened = 0
        result = []

        for variant in variants:
            for letter in variant:
                opened += 1 if letter == "(" else -1
                if opened < 0:
                    break
            if opened == 0:
                result.append("".join(variant))
            opened = 0
        return result


a = Solution()
b = a.generateParenthesis(6)
from pprint import pprint
pprint(b)