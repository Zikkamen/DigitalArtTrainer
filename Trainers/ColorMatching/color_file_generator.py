import os.path
import random

from PIL import ImageDraw, ImageFont, Image
from Models.colour_map import ColourDataPoint
import numpy as np


def generate_uniform_random_numbers() -> np.array:
    return np.random.randint(0, 255, size=3)


def generate_hue_random_number() -> np.array:
    color = np.random.randint(0, 255, size=3)

    indices = np.random.choice(3, 2, replace=False)

    color[indices[0]] = 255
    color[indices[1]] = 0

    return color


class DarknessColorGenerator:
    def __init__(self) -> None:
        self.hue = generate_hue_random_number()
        self.first = False

    def generate_darkness_color(self) -> np.array:
        alpha = random.random()

        if self.first:
            self.first = False
            return self.hue

        return np.int32(alpha * (self.hue + 0.5))

    def set_first_datapoint(self, status: bool) -> None:
        self.first = status


class SaturationColorGenerator:
    def __init__(self) -> None:
        self.hue = generate_hue_random_number()
        self.diff = np.array([255, 255, 255]) - self.hue
        self.first = False

    def generate_saturation_color(self) -> np.array:
        alpha = random.random()

        if self.first:
            self.first = False
            return self.hue

        return self.hue + np.int32(self.diff * alpha + 0.5)

    def generate_saturation_and_darken_color(self) -> np.array:
        alpha = random.random()
        beta = random.random()

        if self.first:
            self.first = False
            return self.hue

        return np.int32((self.hue + np.int32(self.diff * alpha + 0.5)) * beta)

    def set_first_datapoint(self, status: bool):
        self.first = status


class ColorMatcherGenerator:
    def __init__(self) -> None:
        self.darkness_generator = DarknessColorGenerator()
        self.saturation_generator = SaturationColorGenerator()
        self.generator = generate_uniform_random_numbers
        self.name_generator_map = {
            'colour': generate_uniform_random_numbers,
            'hue': generate_hue_random_number,
            'darkness': self.darkness_generator.generate_darkness_color,
            'saturation': self.saturation_generator.generate_saturation_color,
            'satdark': self.saturation_generator.generate_saturation_and_darken_color
        }
        self.font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "../../Arial.ttf"), 75)

    def generate_exercise(self, img_task: Image) -> list:
        draw_task = ImageDraw.Draw(img_task)
        answer_dots = []

        answer_placement = 210
        square_width = 200
        buffer_y = 130
        buffer_x = 35
        counter = 0

        self.setup_generators()

        for i in np.arange(buffer_y, 3580 - buffer_y, 400):
            for j in np.arange(buffer_x, 2480 - buffer_x, 500):
                color = self.generator()

                draw_task.rectangle((j, i, j+square_width, i+square_width), tuple(color), (0, 0, 0), 5)
                draw_task.rectangle((j + answer_placement, i, j + square_width + answer_placement, i + square_width),
                                    (255, 255, 255), (0, 0, 0), 5)

                counter += 1
                draw_task.text((j, i-80), f"#{counter}", (50, 50, 50), self.font)
                answer_dots.append(ColourDataPoint(
                    position=(j + answer_placement + square_width // 2, i + square_width // 2),
                    color=color
                ))

        return answer_dots

    def use_certain_number_generator(self, name: str) -> None:
        if name not in self.name_generator_map:
            raise IOError

        self.generator = self.name_generator_map[name]

    def setup_generators(self) -> None:
        self.darkness_generator.set_first_datapoint(True)
        self.saturation_generator.set_first_datapoint(True)

    def write_score_card(self, img_sol: Image, scores: list):
        buffer_y = 130
        buffer_x = 35
        counter = 0
        draw_task = ImageDraw.Draw(img_sol)

        for i in np.arange(buffer_y, 3580 - buffer_y, 400):
            for j in np.arange(buffer_x, 2480 - buffer_x, 500):
                draw_task.text((j+200, i-80), str(scores[counter]), (50, 50, 50), self.font)
                counter += 1


if __name__ == "__main__":
    img = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))
    cmg = ColorMatcherGenerator()
    cmg.use_certain_number_generator('sat_dark')
    cmg.generate_exercise(img)
    img.show()
