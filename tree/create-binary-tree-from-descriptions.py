from typing import List, Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        child_nodes = {c for _, c, _ in descriptions}
        root = None

        for p, c, l in descriptions:
            parent, child = nodes[p], nodes[c]
            parent.val, child.val = p, c

            if p not in child_nodes:
                root = p

            if l == 1:
                parent.left = child
            else:
                parent.right = child


        return nodes[root]
