# o(1) for increment
class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.inc = [0] * maxSize
        self.stack = [-1] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top >= self.maxSize - 1:
            return

        self.top += 1
        self.stack[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1

        val = self.stack[self.top] + self.inc[self.top]

        if self.top > 0:
            self.inc[self.top - 1] += self.inc[self.top]

        self.inc[self.top] = 0
        self.stack[self.top] = -1
        self.top -= 1
        return val

    def increment(self, k: int, val: int) -> None:
        if self.top == -1:
            return
        idx = min(k, self.top + 1) - 1
        self.inc[idx] += val


# o(k) for increment
# class CustomStack:
#
#     def __init__(self, maxSize: int):
#         self.maxSize = maxSize
#         self.stack = []
#
#     def push(self, x: int) -> None:
#         if len(self.stack) < self.maxSize:
#             self.stack.append(x)
#
#     def pop(self) -> int:
#         if self.stack:
#             return self.stack.pop()
#         return -1
#
#     def increment(self, k: int, val: int) -> None:
#         for i in range(min(k, len(self.stack))):
#             self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
