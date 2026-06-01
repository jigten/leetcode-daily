from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        curr = mass
        for a in sorted(asteroids):
            if a > curr:
                return False

            curr += a

        return True
