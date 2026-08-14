from typing import List


class Node:
    def __init__(self, count=0):
        self.count = count


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [Node()] * (4 * (self.n))
        self.res = [[0, 0] for _ in range(n)]

        if self.n >= 1:
            self._build(0, 0, self.n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = Node(1)
            return

        mid = (start + end) // 2
        left = node * 2 + 1
        right = node * 2 + 2

        self._build(left, start, mid)
        self._build(right, mid + 1, end)

        left_node = self.tree[left]
        right_node = self.tree[right]

        self.tree[node] = Node(left_node.count + right_node.count)

    def update(self, h, k):
        self._update(0, 0, self.n - 1, k + 1, h, k)

    def _update(self, node, start, end, target, h, k):
        if start == end:
            self.tree[node] = Node(0)
            self.res[start] = (h, k)
            return

        mid = (start + end) // 2
        left = node * 2 + 1
        right = node * 2 + 2

        if self.tree[left].count >= target:
            self._update(left, start, mid, target, h, k)
        else:
            self._update(right, mid + 1, end, target - self.tree[left].count, h, k)

        self.tree[node] = Node(self.tree[left].count + self.tree[right].count)


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        st = SegmentTree(n)
        for h, k in sorted(people, key=lambda x: (x[0], -x[1])):
            st.update(h, k)

        return st.res
