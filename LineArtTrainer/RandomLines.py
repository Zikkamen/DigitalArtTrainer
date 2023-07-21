import random

import PIL.ImageDraw
import numpy as np
from PIL import ImageDraw, ImageFont, Image


class RandomLines:
    def __int__(self) -> None:
        pass

    def draw_random_lines(self, img_task: Image, img_task_view: Image, img_answer: Image) -> None:
        draw_task = ImageDraw.Draw(img_task)
        draw_task_view = ImageDraw.Draw(img_task_view)
        draw_answer = ImageDraw.Draw(img_answer)

        for i in range(10):
            pos1 = (random.randint(0, 2480), random.randint(0, 3580))
            pos2 = (random.randint(0, 2480), random.randint(0, 3580))
            color = np.random.randint(50, 255, size=3)

            self.draw_crosses(draw_task, pos1, pos2, 20, color)
            self.draw_crosses(draw_task_view, pos1, pos2, 20, color)

            font = ImageFont.truetype("arial.ttf", 75)
            draw_task_view.text(pos1, str(i + 1), (50, 50, 50), font)
            draw_task_view.text(pos2, str(i + 1), (50, 50, 50), font)

            draw_answer.line(pos1 + pos2, fill=(0, 0, 0), width=10)

    def draw_crosses(self, canvas: PIL.ImageDraw.ImageDraw, pos1: tuple, pos2: tuple, length: int, color: tuple):
        canvas.line((pos1[0] + length, pos1[1] + length, pos1[0] - length, pos1[1] - length), fill=tuple(color), width=10)
        canvas.line((pos1[0] - length, pos1[1] + length, pos1[0] + length, pos1[1] - length), fill=tuple(color), width=10)
        canvas.line((pos2[0] + length, pos2[1] + length, pos2[0] - length, pos2[1] - length), fill=tuple(color), width=10)
        canvas.line((pos2[0] - length, pos2[1] + length, pos2[0] + length, pos2[1] - length), fill=tuple(color), width=10)
