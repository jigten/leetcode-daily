from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.data = nums
        self.tree = [0] * (4 * self.n)

        if self.n > 0:
            self._build(0, 0, self.n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return

        mid = (start + end) // 2
        left = node * 2 + 1
        right = node * 2 + 2

        self._build(left, start, mid)
        self._build(right, mid + 1, end)

        self.tree[node] = self.tree[left] + self.tree[right]

    def update(self, index: int, val: int) -> None:
        self._update(0, 0, self.n - 1, index, val)
        self.data[index] = val

    def _update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val

        mid = (start + end) // 2
        left = node * 2 + 1
        right = node * 2 + 2

        if start <= index <= mid:
            self._update(left, start, mid, index, val)
        else:
            self._update(right, mid + 1, end, index, val)

        self.tree[node] = self.tree[left] + self.tree[right]

    def sumRange(self, left: int, right: int) -> int:
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return self._query(node * 2 + 1, start, mid, left, right) + self._query(
            node * 2 + 2, mid + 1, end, left, right
        )


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
