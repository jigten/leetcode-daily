from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return (0, 0)

            left_steal, left_not_steal = dfs(node.left)
            right_steal, right_not_steal = dfs(node.right)

            rob = node.val + left_not_steal + right_not_steal
            skip = max(left_not_steal, left_steal) + max(right_not_steal, right_steal)

            return (rob, skip)

        return max(dfs(root))
