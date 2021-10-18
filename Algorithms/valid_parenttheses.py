# https://leetcode.com/problems/valid-parentheses/

import time

s = "())"


class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        match_chars = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in match_chars:
                open_stack.append(i)
            else:
                if len(open_stack) == 0:
                    return False
                value = open_stack.pop()
                if match_chars[value] != i:
                    return False
        return open_stack == []


start = time.time()
a = Solution().isValid(s)
finish = time.time() - start
print(a, finish)
