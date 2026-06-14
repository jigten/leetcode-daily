class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        vowels = {"a", "e", "i", "o", "u"}

        def findCntAndIdx(s):
            i = 0
            cnt = 0

            while i < len(s):
                if s[i] == " ":
                    break

                if s[i] in vowels:
                    cnt += 1

                i += 1

            return i + 1, cnt

        def reverse(s, l, r):
            left, right = l, r
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        idx, cnt = findCntAndIdx(s)
        l = r = idx
        curr_cnt = 0

        while r < len(s):
            if s[r] == " ":
                if curr_cnt == cnt:
                    reverse(s, l, r - 1)
                r += 1
                l = r
                curr_cnt = 0

            if s[r] in vowels:
                curr_cnt += 1

            r += 1

        if curr_cnt == cnt:
            reverse(s, l, r - 1)

        return "".join(s)
