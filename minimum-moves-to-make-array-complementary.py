from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diffs = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - i - 1]
            diffs[a + b] -= 1
            diffs[a + b + 1] += 1
            diffs[min(a, b) + 1] -= 1
            diffs[max(a, b) + limit + 1] += 1

        curr = n
        res = n

        for T in range(2, 2 * limit + 1):
            curr += diffs[T]
            res = min(res, curr)

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.minMoves([1, 2, 4, 3], 4) == 1
    assert s.minMoves([1, 2, 2, 1], 2) == 2
    assert s.minMoves([1, 2, 1, 2], 2) == 0
    print("All tests passed!")
