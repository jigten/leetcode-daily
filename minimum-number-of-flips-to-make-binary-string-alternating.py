class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        res = float('inf')
        l, r = 0, 0
        one_odd_cnts, one_even_cnts = 0, 0
        zero_odd_cnts, zero_even_cnts = 0, 0
        s_doubled = s + s

        while r < (n * 2):
            if r >= n:
                if s_doubled[l] == '1':
                    if l % 2:
                        one_odd_cnts -= 1
                    else:
                        one_even_cnts -= 1
                else:
                    if l % 2:
                        zero_odd_cnts -= 1
                    else:
                        zero_even_cnts -= 1
                l += 1

            if s_doubled[r] == '1':
                if r % 2:
                    one_odd_cnts += 1
                else:
                    one_even_cnts += 1
            else:
                if r % 2:
                    zero_odd_cnts += 1
                else:
                    zero_even_cnts += 1
            
            if r >= n - 1:
                res = min(res, min(one_even_cnts + zero_odd_cnts, zero_even_cnts + one_odd_cnts))

            r += 1

        return res