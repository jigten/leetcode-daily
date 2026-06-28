from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res, i = [], 0

        for num in range(1, n + 1):
            curr = target[i]

            if num != curr:
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")
                i += 1

        return res
