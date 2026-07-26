class Solution:
    def minOperations(self, s: str) -> int:
        def numOfOps(s):
            last, cnt = s[0], 0
            for i in range(1, len(s)):
                if s[i] == last:
                    cnt += 1
                    if s[i] == '0':
                        last = '1'
                    else:
                        last = '0'
                else:
                    last = s[i]

            return cnt

        alternate = '1' if s[0] == '0' else '0'
        return min(numOfOps(s), numOfOps(alternate + s[1:]) + 1) 
