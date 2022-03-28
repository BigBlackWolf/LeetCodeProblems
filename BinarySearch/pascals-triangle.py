from typing import Optional, List


class Solution:
    # Recursive
    def generate(self, numRows: int) -> List[List[int]]:
        first = [1]
        if numRows == 1:
            return [first]
        second = first * 2
        result = [first, second]
        for i in range(numRows - 2):
            tmp = 0
            tmp_result = [1]
            for j in result[-1]:
                if tmp == 0:
                    tmp = j
                else:
                    tmp += j
                    tmp_result.append(tmp)
                    tmp = j
            tmp_result.append(1)
            result.append(tmp_result)
        return result


numRows = 5
sol = Solution()
a = sol.generate(numRows)
print(a)
