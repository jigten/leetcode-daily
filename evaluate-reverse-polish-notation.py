from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []

        for t in tokens:
            if t == "+":
                y, x = stack.pop(), stack.pop()
                stack.append(x + y)
            elif t == "-":
                y, x = stack.pop(), stack.pop()
                stack.append(x - y)
            elif t == "*":
                y, x = stack.pop(), stack.pop()
                stack.append(x * y)
            elif t == "/":
                y, x = stack.pop(), stack.pop()
                stack.append(x // y)
            else:
                stack.append(int(t))

        return stack[0]
