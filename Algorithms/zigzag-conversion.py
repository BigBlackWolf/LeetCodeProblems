"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s
        length = len(s) // 2 + 1
        result = [['' for _ in range(length)] for _ in range(numRows)]
        current_row = 0
        current_column = 0
        counter = 0
        direction = True
        for i in range(len(s)):
            result[current_row][current_column] = s[i]
            # diagonal
            if counter == 0:
                if current_row == 0:
                    counter = 1
                    current_row += 1
                elif not direction:
                    current_row -= 1
                    current_column += 1
            # down
            else:
                if counter + 1 != len(result):
                    current_row += 1
                    counter += 1
                else:
                    counter = 0
                    current_row -= 1
                    current_column += 1
                    direction = False
        str_result = ''.join(sum(result, []))
        return str_result
