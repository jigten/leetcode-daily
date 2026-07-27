class MyQueue:

    def __init__(self):
        self.stacks = [], []

    def push(self, x: int) -> None:
        in_stack, _ = self.stacks
        in_stack.append(x)

    def pop(self) -> int:
        in_stack, out_stack = self.stacks

        if not out_stack:
            while in_stack:
                out_stack.append(in_stack.pop())

        return out_stack.pop()

    def peek(self) -> int:
        in_stack, out_stack = self.stacks

        if not out_stack:
            while in_stack:
                out_stack.append(in_stack.pop())

        return out_stack[-1]

    def empty(self) -> bool:
        in_stack, out_stack = self.stacks
        return not in_stack and not out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
