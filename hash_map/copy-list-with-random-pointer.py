from typing import Optional


class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return

        nodes_map = {head: Node(head.val)}
        curr = head

        while curr:
            n = nodes_map[curr]

            if curr.next and curr.next not in nodes_map:
                nodes_map[curr.next] = Node(curr.next.val)

            if curr.random and curr.random not in nodes_map:
                nodes_map[curr.random] = Node(curr.random.val)

            if curr.next:
                n.next = nodes_map[curr.next]

            if curr.random:
                n.random = nodes_map[curr.random]

            curr = curr.next

        return nodes_map[head]
