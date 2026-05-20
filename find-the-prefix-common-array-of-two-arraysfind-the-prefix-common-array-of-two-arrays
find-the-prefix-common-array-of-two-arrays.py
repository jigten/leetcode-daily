from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq_arr = [0] * (n + 1)
        res = [0] * n

        for i, (a, b) in enumerate(zip(A, B)):
            curr = 0
            freq_arr[a] += 1
            freq_arr[b] += 1

            if freq_arr[a] == 2:
                curr += 1

            if a != b and freq_arr[b] == 2:
                curr += 1

            res[i] = res[i - 1] + curr

        return res
