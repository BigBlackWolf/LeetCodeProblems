"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ind = 0
        t_ind = 0
        while t_ind <= len(t) - 1 and s_ind <= len(s) - 1:
            if t[t_ind] == s[s_ind]:
                s_ind += 1
            t_ind += 1
        return s_ind == len(s)


s = "a"
t = "b"
res = Solution().isSubsequence(s, t)
print(res)