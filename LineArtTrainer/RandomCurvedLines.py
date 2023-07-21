import random

import aggdraw
from PIL import Image
import numpy as np


class RandomCurvedLinesGenerator:
    def __int__(self) -> None:
        pass

    def draw_random_curved_lines(self, img_task: Image, img_answer: Image) -> None:

        for i in range(10):
            draw = aggdraw.Draw(img_task)

            ps = np.array([random.randint(0, 2480), random.randint(0, 3580)])
            pe = np.array([random.randint(0, 2480), random.randint(0, 3580)])

            vec_1 = pe - ps
            norm_1 = np.array([-vec_1[1], vec_1[0]])

            alpha = random.random() / 2
            alpha_inv = 1 - alpha

            height = random.random()

            p1 = ps + alpha * vec_1 + height * norm_1
            p2 = ps + alpha_inv * vec_1 - height * norm_1
            
            # pathstring = f"m{ps[0]},{ps[1]} c{p1[0]},{p1[1]},{p2[0]},{p2[1]},{pe[0]},{pe[1]}"

            color = np.random.randint(60, 255, size=3)

            pen = aggdraw.Pen(tuple(color), 10)
            path = aggdraw.Path()

            path.moveto(ps[0], ps[1])
            path.curveto(p1[0], p1[1], p2[0], p2[1], pe[0], pe[1])

            draw.path(path, pen)
            draw.flush()
