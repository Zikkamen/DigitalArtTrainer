from unittest import TestCase

from PIL import Image

from Trainers.LineArt.random_lines import RandomLines


class TestRandomLines(TestCase):
    def test_draw_random_lines(self):
        rl = RandomLines()

        im1 = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))
        im2 = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))

        rl.draw_random_lines(im1, im2)

        assert im1 != Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))
        assert im2 != Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))