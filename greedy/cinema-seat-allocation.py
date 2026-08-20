from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_map = {}

        for r, s in reservedSeats:
            if r not in row_map:
                row_map[r] = [0] * 10
            row_map[r][s - 1] = 1

        res = 0
        res += (n - len(row_map)) * 2

        for r, seats in row_map.items():
            left_free = all(seats[i] == 0 for i in range(1, 5))
            right_free = all(seats[i] == 0 for i in range(5, 9))
            mid_free = all(seats[i] == 0 for i in range(3, 7))

            if left_free and right_free:
                res += 2
            elif left_free or right_free:
                res += 1
            elif mid_free:
                res += 1

        return res
