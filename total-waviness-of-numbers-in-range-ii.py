from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(num):
            n_str = str(num)

            @lru_cache(None)
            def dfs(idx, is_tight, is_zero, prev2, prev):
                if idx == len(n_str):
                    return 1, 0

                limit = 9
                if is_tight:
                    limit = int(n_str[idx])

                total_sub, total_waviness = 0, 0

                for d in range(limit + 1):
                    new_tight = is_tight and d == limit
                    new_zero = is_zero and d == 0

                    sub_count, sub_waviness = dfs(idx + 1, new_tight, new_zero, -1 if new_zero else prev, -1 if new_zero else d)

                    is_wave = False
                    if not is_zero and prev2 != -1 and prev != -1:
                        if (prev2 > prev < d) or (prev2 < prev > d):
                            is_wave = True

                    total_sub += sub_count
                    total_waviness += sub_waviness + (sub_count if is_wave else 0)


                return total_sub, total_waviness

            return dfs(0, True, True, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)
