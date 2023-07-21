import random

import numpy as np
from PIL import ImageDraw, ImageFont, Image


class RandomLines:
    def __int__(self) -> None:
        pass

    def draw_random_lines(self, img_task: Image, img_answer: Image) -> None:
        draw_task = ImageDraw.Draw(img_task)
        draw_answer = ImageDraw.Draw(img_answer)

        for i in range(10):
            x1 = random.randint(0, 2480)
            y1 = random.randint(0, 3580)
            x2 = random.randint(0, 2480)
            y2 = random.randint(0, 3580)

            color = np.random.randint(50, 255, size=3)

            x_length = 20

            draw_task.line((x1 + x_length, y1 + x_length, x1 - x_length, y1 - x_length), fill=tuple(color), width=10)
            draw_task.line((x1 - x_length, y1 + x_length, x1 + x_length, y1 - x_length), fill=tuple(color), width=10)
            draw_task.line((x2 + x_length, y2 + x_length, x2 - x_length, y2 - x_length), fill=tuple(color), width=10)
            draw_task.line((x2 - x_length, y2 + x_length, x2 + x_length, y2 - x_length), fill=tuple(color), width=10)

            font = ImageFont.truetype("arial.ttf", 75)
            draw_task.text((x1, y1), str(i + 1), (50, 50, 50), font)
            draw_task.text((x2, y2), str(i + 1), (50, 50, 50), font)

            draw_answer.line((x1, y1, x2, y2), fill=(0, 0, 0), width=10)