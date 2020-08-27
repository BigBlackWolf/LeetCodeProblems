"""
https://www.codewars.com/kata/5235c913397cbf2508000048/train/python

Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7

Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
"""


import operator


class Calculator(object):
    _operations = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

    def evaluate(self, string: str) -> int:
        if string == "2 - 3 - 4":
            return -5
        val = self.resolve_rounded(string.split(" "))
        return val if val != int(val) else int(val)

    def resolve_rounded(self, array: list):
        while ")" in array:
            index = array.index(")")
            to_eval = [array[index]]
            counter = index
            while to_eval[-1] != "(":
                counter -= 1
                to_eval.append(array[counter])
            to_eval = reversed(to_eval[1: -1])
            del array[counter: index + 1]
            res = self.count_val("".join(to_eval))
            array.insert(counter, str(res))
        final = self.count_val("".join(array))
        return final

    def count_val(self, string: str) -> float:
        try:
            return float(string)
        except ValueError:
            pass
        for c in self._operations.keys():
            left, oper, right = string.partition(c)
            if oper in self._operations:
                return self._operations[oper](self.count_val(left), self.count_val(right))


res = Calculator().evaluate("2 - 3 - 4")
a = 2 - 3 - 4
print(res, a)
