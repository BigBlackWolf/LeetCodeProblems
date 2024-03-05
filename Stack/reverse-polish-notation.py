"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        specials = {"/", "*", "+", "-"}
        for t in tokens:
            if t not in specials:
                stack.append(int(t))
            else:
                first = int(stack.pop())
                second = int(stack.pop())
                if t == "/":
                    stack.append(int(second / first))
                elif t == "*":
                    stack.append(second * first)
                elif t == "+":
                    stack.append(second + first)
                elif t == "-":
                    stack.append(second - first)
        return stack[0]


t1 = ["2","1","+","3","*"]
t2 = ["4","13","5","/","+"]
t3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

res = Solution().evalRPN(t3)
print(res)
    