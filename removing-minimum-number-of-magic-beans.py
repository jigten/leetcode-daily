from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        total_cost_to_reduce_all_to_zero = sum(beans)
        res = float("inf")
        n = len(beans)

        # now we will calculate the max cost needed to make all beans equal to each bean
        # subtracting that from total_cost_to_reduce_all_to_zero will give us the min
        for i, b in enumerate(sorted(beans)):
            res = min(res, total_cost_to_reduce_all_to_zero - ((n - i) * b))

        return res
