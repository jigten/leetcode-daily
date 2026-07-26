from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        res = []
        vowels = {'a', 'e', 'i', 'o', 'u'}

        prefix_cnts = [0] * n
        cnts = 0

        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                cnts += 1
                prefix_cnts[i] = cnts
            else:
                prefix_cnts[i] = cnts

        for q1, q2 in queries:
            if q1 > 0:
                res.append(prefix_cnts[q2] - prefix_cnts[q1 - 1])
            else:
                res.append(prefix_cnts[q2])

        return res
