"""
https://www.codewars.com/kata/526989a41034285187000de4/train/python

Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.
Examples

ips_between("10.0.0.0", "10.0.0.50")  ==   50
ips_between("10.0.0.0", "10.0.1.0")   ==  256
ips_between("20.0.0.10", "20.0.1.0")  ==  246
"""


def ips_between(start, end) -> int:
    start_bits = start.split(".")
    start_bits = list(map(lambda x: int(x), start_bits))
    end_bits = end.split(".")
    end_bits = list(map(lambda x: int(x), end_bits))
    multiply = 0
    for i in range(len(start_bits)):
        if multiply != 0:
            multiply *= 256
        multiply += end_bits[i] - start_bits[i]
    return multiply


a = ips_between("10.0.0.0", "10.0.0.50")
b = ips_between("20.0.0.10", "20.0.1.0")
print(a, b)
