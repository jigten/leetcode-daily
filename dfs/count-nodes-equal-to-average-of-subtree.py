# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0, 0

            l_cnt, l_sum = dfs(node.left)
            r_cnt, r_sum = dfs(node.right)

            sum_ = l_sum + r_sum + node.val
            cnt_ = l_cnt + r_cnt + 1

            if sum_ // cnt_ == node.val:
                self.res += 1

            return cnt_, sum_

        dfs(root)

        return self.res
