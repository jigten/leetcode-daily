from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        odd = head
        evenHead = odd.next
        even = evenHead

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = odd.next

        odd.next = evenHead

        return head
