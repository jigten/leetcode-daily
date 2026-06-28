from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        counts = [0] * (n + 1)

        for num in arr:
            counts[min(num, n)] += 1

        res = 1

        for i in range(2, n + 1):
            res = min(res + counts[i], i)
        
        return res

        sorted_arr = sorted(arr)
        res = 1

        for i in range(1, len(sorted_arr)):
            if sorted_arr[i] >= res + 1:
                res += 1

        return res
