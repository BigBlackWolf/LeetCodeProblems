class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs:
            return ""
        first = strs.pop(0)
        for i in range(len(first)):
            to_test = first[:i + 1]
            test = map(lambda x: x.startswith(to_test), strs)
            if not all(test):
                return to_test[:-1]
        return first


arr = ["aff", "fs", "fa"]  # "fl"
arr2 = ["dog", "racecar", "car"]  # ""

a = Solution().longestCommonPrefix(arr)
print(a)
