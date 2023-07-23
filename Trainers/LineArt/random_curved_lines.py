import random

import aggdraw
from PIL import Image
import numpy as np


def generate_vector_and_normal(pos1: np.array, pos2: np.array):
    vec = pos2 - pos1

    return vec, np.array([-vec[1], vec[0]])


def generate_random_pos() -> np.array:
    return np.array([random.randint(0, 2480), random.randint(0, 3580)])


def generate_two_random_pos() -> tuple:
    return generate_random_pos(), generate_random_pos()


def generate_two_positions(pos: np.array, vec: np.array, norm: np.array) -> tuple:
    height = random.random()
    alpha = random.random() / 2

    return pos + alpha * vec + height * norm, pos + (1-alpha) * vec - height * norm


class RandomCurvedLinesGenerator:
    def __int__(self) -> None:
        pass

    def draw_random_curved_lines(self, img_task: Image, img_answer: Image) -> None:
        for i in range(15):
            draw = aggdraw.Draw(img_task)

            pos_start, pos_end = generate_two_random_pos()
            vec_1, norm_1 = generate_vector_and_normal(pos_start, pos_end)
            p1, p2 = generate_two_positions(pos_start, vec_1, norm_1)

            color = np.random.randint(60, 255, size=3)

            pen = aggdraw.Pen(tuple(color), 10)
            path = aggdraw.Path()

            path.moveto(pos_start[0], pos_start[1])
            path.curveto(p1[0], p1[1], p2[0], p2[1], pos_end[0], pos_end[1])

            draw.path(path, pen)
            draw.flush()
