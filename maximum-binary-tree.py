from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        # stack o(n)
        stack = []

        for n in nums:
            node = TreeNode(n)

            while stack and stack[-1].val < n:
                node.left = stack.pop()

            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]

        # recursive o(n^2)
        def build(l, r):
            if l >= r:
                return None

            max_val = max(nums[l:r])
            mi = nums.index(max_val, l, r)
            node = TreeNode(nums[mi])
            node.left = build(l, mi)
            node.right = build(mi + 1, r)

            return node

        return build(0, n)
