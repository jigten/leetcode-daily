from typing import List


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0

        def getDigits(num: int) -> List[int]:
            digits = []

            while num > 0:
                digits.append(num % 10)
                num //= 10

            return digits


        for n in range(num1, num2 + 1):
            digits = getDigits(n)

            for i in range(1, len(digits) - 1):
                if digits[i - 1] < digits[i] > digits[i + 1]:
                    res += 1

                if digits[i - 1] > digits[i] < digits[i + 1]:
                    res += 1


        return res
