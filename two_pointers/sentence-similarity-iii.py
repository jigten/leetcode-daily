from collections import deque


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        q1, q2 = deque(sentence1.split(" ")), deque(sentence2.split(" "))

        while q1 and q2 and (q1[0] == q2[0] or q1[-1] == q2[-1]):
            if q1[0] == q2[0]:
                q1.popleft()
                q2.popleft()
            else:
                q1.pop()
                q2.pop()

        return len(q1) == 0 or len(q2) == 0
