"""
https://www.codewars.com/kata/581bc0629ad9ff9873000316/train/python

This calculator takes values that could be written in a browsers route path as a single string. It then returns the result as a number (or an error message).

Route paths use the '/' symbol so this can't be in our calculator. Instead we are using the '$' symbol as our divide operator.

You will be passed a string of any length containing numbers and operators:

    '+' = add
    '-' = subtract
    '*' = multiply
    '$' = divide

Your task is to break the string down and calculate the expression using this order of operations. (division => multiplication => subtraction => addition)

If you are given an invalid input (i.e. any character except .0123456789+-*$) you should return the error message:'400: Bad request'
Remember:

    Operations are infinite
    Order of operations is imperitive
    No eval or equivalent functions

Examples:

calculate('1+1')     => '2'
calculate('10$2')    => '5'
calculate('1.5*3')   => '4.5'

calculate('5+5+5+5') => '20'

calculate('1000$2.5$5+5-5+6$6') =>'81'

calculate('10-9p')   =>  '400: Bad request'
"""
import re
import operator

operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "$": operator.truediv}


def calculate(expression):
    if re.search(r"[^.0-9\-\+\*\.\$]", expression):
        return "400: Bad request"
    data = re.findall(r"[0-9\.]+", expression)
    data = list(map(lambda x: float(x) if '.' in x else int(x), data))
    signs = re.findall(r"[\+\-\$\*]", expression)
    priors = list(filter(lambda x: re.match(r"[\*\$]", x), signs))

    while len(data) != 1:
        sign_index = signs.index(priors.pop(0)) if priors else 0
        oper = signs.pop(sign_index)
        first = data.pop(sign_index)
        second = data.pop(sign_index)
        data.insert(sign_index, operators[oper](first, second))

    result = data[0] if int(data[0]) != data[0] else int(data[0])
    return result


tests = [
    ["1.1", 1.1],                   # returns the number if no commands given
    ["10+5", 15],                   # addition
    ["8-2", 6],                     # subtraction
    ["4*3", 12],                    # muliplication
    ["18$2", 9],                    # division
    ["5+8-8*2$4", 9],               # multiple commands
    ["3x+1", "400: Bad request"]    # handles incorrect input
]

calculate("5+8-8*2$4")

# for test in tests:
#     assert calculate(test[0]) == test[1]