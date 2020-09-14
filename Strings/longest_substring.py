class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        start = 0
        max_length = 0
        for i in s:
            chars.append(i)
            index_ = chars.index(i, start)
            if index_ != len(chars) - 1:
                start = index_ + 1
            max_length = max(len(chars) - start, max_length)
        return max_length

