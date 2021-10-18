# https://leetcode.com/problems/longest-palindromic-substring/

import time


s = "abaad"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        structure = {}
        longest_string = ""
        for i in range(len(s)):
            if s[i] in structure:
                structure[s[i]].append(i)
            else:
                structure[s[i]] = [i]

        for i in range(len(s)):
            elements = structure[s[i]]
            for j in elements[::-1]:
                if j > i:
                    if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(longest_string):
                        longest_string = s[i:j+1]
                        if len(longest_string) == len(s):
                            break
                else:
                    continue
            else:
                continue
            break
        if longest_string == "":
            longest_string = s[0]
        return longest_string


start = time.time()
a = Solution().longestPalindrome(s)
finish = time.time() - start
print(a, finish)
print(len(s))
