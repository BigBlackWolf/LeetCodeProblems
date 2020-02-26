"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True for _ in range(n - 1)]
        step = 2
        while step * step <= n:
            if primes[step - 2]:
                tmp = step + step - 2
                while tmp < n - 1:
                    primes[tmp] = False
                    tmp += step
            step += 1
        result = list(filter(lambda x: x, primes[:-1]))
        return len(result)
