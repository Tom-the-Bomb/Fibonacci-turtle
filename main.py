from turtle import Turtle, circle
import random

class Fibonacci:
    COLORS = ('red', 'orange', 'green', 'purple', 'blue')

    def _reset_fib(self) -> None:
        self._previous_2 = 0
        self._previous_1 = 1
        self._next = 1

    def _update_fib(self) -> None:
        self._next = self._previous_1 + self._previous_2
        self._previous_2 = self._previous_1
        self._previous_1 = self._next

    def __init__(self) -> None:
        self.turtle = Turtle()
        self.turtle.speed(10)
        self._reset_fib()

    def draw(self, n: int) -> None:
        for _ in range(n):
            self.turtle.color(random.choice(self.COLORS))
            for i in range(6):
                self.turtle.forward(self._next)
                if i < 5:
                    self.turtle.left(90)
            self._update_fib()

        self.turtle.hideturtle()
        self._reset_fib()

        self.turtle.color('black')
        for _ in range(n):
            circle(self._next, 90)
            self._update_fib()

def main() -> None:
    while True:
        try:
            n = int(input('Enter pattern length: '))
            break
        except ValueError:
            continue
    Fibonacci().draw(n)

if __name__ == '__main__':
    main()