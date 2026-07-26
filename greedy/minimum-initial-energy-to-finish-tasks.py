from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        energy = 0

        for a, r in tasks:
            energy = max(r, a + energy)

        return energy
