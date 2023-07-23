import random

from PIL import ImageDraw, ImageFont, Image
import numpy as np


def generate_uniform_random_numbers() -> np.array:
    return np.random.randint(0, 255, size=3)


def generate_hue_random_number() -> np.array:
    color = np.random.randint(0, 255, size=3)
    color[random.randint(0, 2)] = 255

    return color


class DarknessColorGenerator:
    def __init__(self) -> None:
        self.hue = generate_hue_random_number()

    def generate_darkness_color(self) -> np.array:
        alpha = random.random()

        return np.int32(alpha * (self.hue + 0.5))


class SaturationColorGenerator:
    def __init__(self) -> None:
        self.hue = generate_hue_random_number()
        self.diff = np.array([255, 255, 255]) - self.hue

    def generate_saturation_color(self) -> np.array:
        alpha = random.random()

        return self.hue + np.int32(self.diff * alpha + 0.5)


class ColorMatcherGenerator:
    def __init__(self) -> None:
        self.darkness_generator = DarknessColorGenerator()
        self.saturation_generator = SaturationColorGenerator()
        self.generator = generate_uniform_random_numbers
        self.name_generator_map = {
            'uniform': generate_uniform_random_numbers,
            'hue': generate_hue_random_number,
            'darkness': self.darkness_generator.generate_darkness_color,
            'saturation': self.saturation_generator.generate_saturation_color
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
    cmg.use_certain_number_generator('saturation')
    cmg.generate_file(img)
    img.show()
