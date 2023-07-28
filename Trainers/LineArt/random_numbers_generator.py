import numpy as np


def generate_random_rgb_color(low_value: int = 50, high_value: int = 255) -> np.ndarray:
    return np.random.randint(low_value, high_value, size=3)


class RandomNumbersGenerator:
    def __init__(self, range_x: int = 2480, range_y: int = 3580):
        self.range_x = range_x
        self.range_y = range_y

    def generate_random_pos(self) -> np.array:
        return np.array([np.random.randint(0, self.range_x), np.random.randint(0, self.range_y)])

    def generate_two_random_pos(self) -> tuple:
        return self.generate_random_pos(), self.generate_random_pos()
