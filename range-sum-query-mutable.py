from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
            return

        mid = (start + end) // 2
        self._build(2 * node, start, mid)  # build left
        self._build(2 * node + 1, mid + 1, end)  # build right

        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
        return

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2

        if idx <= mid:
            self._update(2 * node, start, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)

        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, index: int, val: int) -> None:
        self._update(1, 0, self.n - 1, index, val)

    def _query(self, node, start, end, left, right):
        if end < left or start > right:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2

        return self._query(node * 2, start, mid, left, right) + self._query(
            node * 2 + 1, mid + 1, end, left, right
        )

    def sumRange(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n - 1, left, right)
