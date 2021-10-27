""" https://leetcode.com/problems/group-anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for item in strs:
            letters = "".join(sorted(item))
            if letters in anagrams:
                anagrams[letters].append(item)
            else:
                anagrams[letters] = [item]
        return [anagrams[key] for key in anagrams]


strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution().groupAnagrams(strs)
print(sol)

