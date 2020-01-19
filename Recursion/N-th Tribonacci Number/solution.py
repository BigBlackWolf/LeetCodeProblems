class Solution:
    zero = 0
    first = 1
    second = 1
    step = 0
    result = 0

    def tribonacci(self, n: int) -> int:
        if n > 3:
            if self.step == 0:
                self.step += 3
                self.result = self.first + self.second + self.zero
            if self.step % 3 == 0:
                self.zero = self.result
                self.result = self.zero + self.first + self.second
            elif self.step % 3 == 1:
                self.first = self.result
                self.result = self.zero + self.first + self.second
            elif self.step % 3 == 2:
                self.second = self.result
                self.result = self.zero + self.first + self.second
            self.step += 1
            if self.step < n:
                self.tribonacci(n)
            return self.result
        elif n == 3:
            return 2
        elif n == 2:
            return 1
        elif n == 1:
            return 1
        elif n == 0:
            return 0