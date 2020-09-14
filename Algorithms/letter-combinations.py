from itertools import product


class Solution:
    _letters = {
        "1": "", "2": "abc", "3": "def",
        "4": "ghi", "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz",
        "0": " "
    }

    def letterCombinations(self, digits: str) -> list:
        stash = []
        if not digits:
            return stash
        for digit in digits:
            stash.append(self._letters[digit])
        shuffled = product(*stash)
        return list(map(lambda x: "".join(x), shuffled))


digits = ""
a = Solution().letterCombinations(digits)
print(a)
