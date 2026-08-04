class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.size >= self.k:
            return False

        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.q[self.head] = -1
        self.head = (self.head + 1) % self.k
        self.size -= 1

        return True

    def Front(self) -> int:
        return self.q[self.head]

    def Rear(self) -> int:
        return self.q[(self.tail - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
