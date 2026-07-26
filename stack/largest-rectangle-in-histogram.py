class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, ht in enumerate(heights):
            start = i

            while stack and stack[-1][0] > ht:
                lht, li = stack.pop()
                area = lht * (i - li)
                res = max(res, area)
                start = li

            stack.append((ht, start))

        while stack:
            lht, li = stack.pop()
            area = lht * (len(heights) - li)
            res = max(res, area)

        return res
