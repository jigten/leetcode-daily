from typing import List


class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = (2 * width + 2 * height) - 4
        self.total_steps = 0
        self.pos = [0, 0]
        self.dir = "East"

    def _move_robot(self):
        if self.total_steps == 0:
            self.pos, self.dir = [0, 0], "East"
            return

        remaining_steps = self.total_steps % self.perimeter

        if remaining_steps == 0:
            self.pos, self.dir = [0, 0], "South"
            return

        w, h = self.width, self.height

        if 1 <= remaining_steps <= w - 1:
            self.pos = [remaining_steps, 0]
            self.dir = "East"
        elif w <= remaining_steps <= (w - 1) + (h - 1):
            self.pos = [w - 1, remaining_steps - (w - 1)]
            self.dir = "North"
        elif (w - 1) + (h - 1) < remaining_steps <= 2 * (w - 1) + (h - 1):
            self.pos = [(w - 1) - (remaining_steps - (w - 1) - (h - 1)), h - 1]
            self.dir = "West"
        else:
            self.pos = [0, (h - 1) - (remaining_steps - (2 * (w - 1) + (h - 1)))]
            self.dir = "South"

    def step(self, num: int) -> None:
        self.total_steps += num

    def getPos(self) -> List[int]:
        self._move_robot()
        return self.pos

    def getDir(self) -> str:
        self._move_robot()
        return self.dir
