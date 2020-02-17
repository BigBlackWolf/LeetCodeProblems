class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        sum = 0
        last = 0
        tmp = 0
        for i in s:
            if tmp != 0:
                tmp -= symbols[i]
                sum += tmp
                tmp = 0
            elif symbols[i] >= last:
                sum += symbols[i]
                last = symbols[i]
            else:
                sum -= symbols[i]
                last = 0

        return sum

