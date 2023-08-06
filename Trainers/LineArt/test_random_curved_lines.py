from unittest import TestCase
from Trainers.LineArt.random_curved_lines import *


class Test(TestCase):
    def test_generate_vector_and_normal(self):
        v1 = np.array([0, 1])
        v2 = np.array([1, 0])

        a1, a2 = generate_vector_and_normal(v1, v2)

        assert all(a1 == np.array([1, -1]))
        assert all(a2 == np.array([1, 1]))

    def test_generate_two_positions(self):
        v1 = np.array([1, -1])
        v2 = np.array([1, 1])

        a1 = generate_two_positions(np.array([0, 0]), v1, v2)

        assert len(a1) == 2

    def test_generate_exercise(self):
        rcg = RandomCurvedLinesGenerator()

        im = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))
        rcg.generate_exercise(im)

        assert im != Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))