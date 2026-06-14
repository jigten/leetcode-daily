from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while head and prev:
            res = max(res, head.val + prev.val)
            head = head.next
            prev = prev.next

        return res
