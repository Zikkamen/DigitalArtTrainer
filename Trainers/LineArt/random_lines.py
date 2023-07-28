import random
import numpy as np

from PIL import ImageDraw, ImageFont, Image
from random_numbers_generator import RandomNumbersGenerator, generate_random_rgb_color


def draw_crosses(canvas: PIL.ImageDraw.ImageDraw, pos1: tuple, pos2: tuple, length: int, color: np.ndarray) -> None:
    canvas.line((pos1[0] + length, pos1[1] + length, pos1[0] - length, pos1[1] - length), fill=tuple(color), width=10)
    canvas.line((pos1[0] - length, pos1[1] + length, pos1[0] + length, pos1[1] - length), fill=tuple(color), width=10)
    canvas.line((pos2[0] + length, pos2[1] + length, pos2[0] - length, pos2[1] - length), fill=tuple(color), width=10)
    canvas.line((pos2[0] - length, pos2[1] + length, pos2[0] + length, pos2[1] - length), fill=tuple(color), width=10)


class RandomLines:
    def __int__(self) -> None:
        self.random_position_generator = RandomNumbersGenerator()

    def draw_random_lines(self, img_task: Image, img_task_view: Image, img_answer: Image) -> None:
        draw_task = ImageDraw.Draw(img_task)
        draw_task_view = ImageDraw.Draw(img_task_view)
        draw_answer = ImageDraw.Draw(img_answer)

        font = ImageFont.truetype("arial.ttf", 75)

        for i in range(10):
            pos1, pos2 = self.random_position_generator.generate_two_random_pos()
            color = generate_random_rgb_color()

            draw_crosses(draw_task, pos1, pos2, 20, color)
            draw_crosses(draw_task_view, pos1, pos2, 20, color)

            draw_task_view.text(pos1, str(i + 1), (50, 50, 50), font)
            draw_task_view.text(pos2, str(i + 1), (50, 50, 50), font)

            draw_answer.line(pos1 + pos2, fill=(0, 0, 0), width=10)
