from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)
        pre, suf = [0] * (m + 1), [0] * (m + 1)

        j = 0
        for i in range(m):
            pre[i + 1] = pre[i]
            if j < n and word1[i] == word2[j]:
                pre[i + 1] += 1
                j += 1

        j = n - 1
        for i in range(m - 1, -1, -1):
            suf[i] = suf[i + 1]
            if j >= 0 and word1[i] == word2[j]:
                suf[i] += 1
                j -= 1

        mx = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            mx[i] = max(pre[i] + suf[i + 1], mx[i + 1])

        res = []
        pos = 0
        budget = 1
        for j in range(n):
            chosen = -1

            for i in range(pos, m):
                if word1[i] == word2[j]:
                    if budget == 1 and mx[i + 1] >= n - 1:
                        chosen = i
                        break
                    if budget == 0 and suf[i + 1] >= n - j - 1:
                        chosen = i
                        break
                else:
                    if budget == 1 and suf[i + 1] >= n - j - 1:
                        chosen = i
                        budget = 0
                        break
            if chosen == -1:
                return []
            res.append(chosen)
            pos = chosen + 1

        return res
