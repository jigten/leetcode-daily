from typing import List


class Node:
    def __init__(self, left_char, right_char, prefix_len, suffix_len, best_len, length):
        self.left_char = left_char
        self.right_char = right_char
        self.prefix_len = prefix_len
        self.suffix_len = suffix_len
        self.best_len = best_len
        self.length = length


class SegmentTree:
    def __init__(self, s: str):
        self.data = list(s)
        self.n = len(self.data)
        self.tree = [0] * (4 * self.n)

        if self.n > 0:
            self._build(0, 0, self.n - 1)

    def _merge(self, L, R):
        prefix = L.prefix_len
        if L.length == L.prefix_len and L.right_char == R.left_char:
            prefix = L.length + R.prefix_len
        suffix = R.suffix_len
        if R.length == R.suffix_len and L.right_char == R.left_char:
            suffix = R.length + L.suffix_len

        best = max(L.best_len, R.best_len)
        if L.right_char == R.left_char:
            best = max(best, L.suffix_len + R.prefix_len)
        return Node(
            L.left_char, R.right_char, prefix, suffix, best, L.length + R.length
        )

    def _build(self, node, start, end):
        if start == end:
            ch = self.data[start]
            self.tree[node] = Node(ch, ch, 1, 1, 1, 1)
            return

        mid = (start + end) // 2
        left = node * 2 + 1
        right = node * 2 + 2

        self._build(left, start, mid)
        self._build(right, mid + 1, end)
        self.tree[node] = self._merge(self.tree[left], self.tree[right])

    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)
        self.data[index] = value

    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node].left_char = value
            self.tree[node].right_char = value
            return

        mid = (start + end) // 2
        left = node * 2 + 1
        right = node * 2 + 2

        if start <= index <= mid:
            self._update(left, start, mid, index, value)
        else:
            self._update(right, mid + 1, end, index, value)

        self.tree[node] = self._merge(self.tree[left], self.tree[right])


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        st = SegmentTree(s)
        res = []

        for c, idx in zip(queryCharacters, queryIndices):
            st.update(idx, c)
            res.append(st.tree[0].best_len)

        return res
