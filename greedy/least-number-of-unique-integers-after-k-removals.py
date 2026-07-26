from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnts = Counter(arr)
        cnts_sorted = sorted(
            [(n, v) for n, v in cnts.items()], key=lambda x: x[1], reverse=True
        )

        while k > 0 and cnts_sorted:
            n, v = cnts_sorted[-1]
            if v <= k:
                k -= v
                cnts_sorted.pop()
            else:
                break

        return len(cnts_sorted)


solution = Solution()
assert solution.findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1) == 1
assert solution.findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3) == 2
