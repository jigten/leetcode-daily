from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        res = [0] * n
        stack = []
        i = 0

        curr = head

        while curr:
            curr_val = curr.val

            while stack and stack[-1][0] < curr_val:
                _, idx = stack.pop()
                res[idx] = curr_val

            stack.append((curr_val, i))
            curr = curr.next
            i += 1

        return res
