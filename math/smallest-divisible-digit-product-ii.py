class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        PILES = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        tf = [0, 0, 0, 0]
        tc = t
        for p, idx in ((2, 0), (3, 1), (5, 2), (7, 3)):
            while tc % p == 0:
                tc //= p
                tf[idx] += 1
        if tc > 1:
            return "-1"

        memo = {}

        def min_digits(r):
            if r == (0, 0, 0, 0):
                return 0
            if r in memo:
                return memo[r]
            best = 10**9
            for d in range(2, 10):
                pile = PILES[d]
                nr = tuple(max(0, r[k] - pile[k]) for k in range(4))
                if nr == r:
                    continue
                best = min(best, 1 + min_digits(nr))
            memo[r] = best
            return best

        n = len(num)
        prefix_piles = [(0, 0, 0, 0)] * (n + 1)
        has_zero = [False] * (n + 1)
        for i in range(n):
            d = int(num[i])
            pp = prefix_piles[i]
            pile = PILES[d] if d != 0 else (0, 0, 0, 0)
            prefix_piles[i + 1] = tuple(pp[k] + pile[k] for k in range(4))
            has_zero[i + 1] = has_zero[i] or (d == 0)

        if not has_zero[n]:
            total = prefix_piles[n]
            if all(total[k] >= tf[k] for k in range(4)):
                return num

        def residual(acc):
            return tuple(max(0, tf[k] - acc[k]) for k in range(4))

        def build_suffix(r, m):
            res = []
            for pos in range(m):
                for d in range(1, 10):
                    pile = PILES[d]
                    nr = tuple(max(0, r[k] - pile[k]) for k in range(4))
                    if min_digits(nr) <= m - pos - 1:
                        res.append(str(d))
                        r = nr
                        break
            return "".join(res)

        for i in range(n - 1, -1, -1):
            if has_zero[i]:
                continue
            m = n - i - 1
            for d in range(int(num[i]) + 1, 10):
                acc = tuple(prefix_piles[i][k] + PILES[d][k] for k in range(4))
                r = residual(acc)
                if min_digits(r) <= m:
                    return num[:i] + str(d) + build_suffix(r, m)

        L = max(n + 1, min_digits(tuple(tf)))
        return build_suffix(tuple(tf), L)
