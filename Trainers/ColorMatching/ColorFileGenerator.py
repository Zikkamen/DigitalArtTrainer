import random

from PIL import ImageDraw, ImageFont, Image
import numpy as np


def generate_uniform_random_numbers() -> np.array:
    return np.random.randint(0, 255, size=3)


def generate_hue_random_number() -> np.array:
    color = np.random.randint(0, 255, size=3)
    color[random.randint(0, 2)] = 255

    return color


class ColorMatcherGenerator:
    def __init__(self) -> None:
        self.generator = generate_uniform_random_numbers
        self.name_generator_map = {
            'uniform': generate_uniform_random_numbers,
            'hue': generate_hue_random_number
        }

    def generate_file(self, img_task: Image) -> list:
        draw_task = ImageDraw.Draw(img_task)
        answer_dots = []

        answer_placement = 210
        square_width = 200

        for i in np.arange(100, 3580-100, 400):
            for j in np.arange(35, 2480-100, 500):
                color = self.generator()

                draw_task.rectangle((j, i, j+square_width, i+square_width), tuple(color), (0, 0, 0), 5)
                draw_task.rectangle((j + answer_placement, i, j + square_width + answer_placement, i + square_width),
                                    (255, 255, 255), (0, 0, 0), 5)

                answer_dots.append((j + answer_placement + square_width // 2, i + square_width // 2))

        return answer_dots

    def use_certain_number_generator(self, name: str) -> None:
        self.generator = self.name_generator_map[name]


if __name__ == "__main__":
    img = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))
    cmg = ColorMatcherGenerator()
    cmg.use_certain_number_generator('hue')
    cmg.generate_file(img)
    img.show()
