from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # o(n) time and o(1) space
        def reverse(node):
            prev, curr = None, node

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        rev_head = reverse(head)

        prev, curr = None, rev_head
        max_ = 0

        while curr:
            max_ = max(max_, curr.val)

            if curr.val < max_:
                prev.next = curr.next
                deleted = curr
                curr = curr.next
                deleted.next = None
            else:
                prev = curr
                curr = curr.next

        return reverse(rev_head)

        # o(n) time and o(n) space
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        curr = stack.pop()
        max_val = curr.val
        res = ListNode(max_val)

        while stack:
            next_node = stack.pop()

            if next_node.val >= max_val:
                max_val = next_node.val
                new_node = ListNode(max_val)
                new_node.next = res
                res = new_node

        return res
