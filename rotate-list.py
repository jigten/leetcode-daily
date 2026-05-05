from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head

        tail.next = head  # form circle
        steps_to_new_tail = n - k

        tail = head
        for _ in range(steps_to_new_tail - 1):
            tail = tail.next

        new_head = tail.next
        tail.next = None

        return new_head
