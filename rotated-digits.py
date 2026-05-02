class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        L = len(s)

        dp = [[[0] * 2 for _ in range(2)] for _ in range(L + 1)]
        dp[0][1][0] = 1

        for i in range(L):
            for tight in range(2):
                for diff in range(2):
                    if dp[i][tight][diff] == 0: continue

                    upper_limit = int(s[i]) if tight else 9

                    for d in range(upper_limit + 1):
                        if d in (3, 4, 7): continue
                        new_tight = tight and d == upper_limit
                        new_diff = diff or d in (2, 5, 6, 9)

                        dp[i + 1][new_tight][new_diff] += dp[i][tight][diff]

        return dp[-1][0][1] + dp[-1][1][1]

        memo = {}

        def dp(pos, is_tight, is_diff):
            if pos == len(s):
                return 1 if is_diff else 0

            cache_key = (pos, is_tight, is_diff)

            if cache_key in memo:
                return memo[cache_key]

            upper_limit = int(s[pos]) if is_tight else 9
            path_sum = 0

            for i in range(upper_limit + 1):
                if i in (3, 4, 7):
                    continue
                new_is_tight = is_tight and i == upper_limit
                new_is_diff = is_diff or i in (2, 5, 6, 9)
                path_sum += dp(pos + 1, new_is_tight, new_is_diff)

            memo[cache_key] = path_sum
            return path_sum

        return dp(0, True, False)

        res = 0

        for i in range(1, n + 1):
            curr = i
            changed = False
            valid = True

            while curr > 0 and valid:
                digit = curr % 10

                if digit in (3, 4, 7):
                    valid = False
                elif digit in (2, 5, 6, 9):
                    changed = True

                curr //= 10

            if valid and changed:
                res += 1

        return res


solution = Solution()
assert solution.rotatedDigits(n=10) == 4
assert solution.rotatedDigits(n=1) == 0
assert solution.rotatedDigits(n=2) == 1
