from unittest import TestCase

from Trainers.LineArt.random_numbers_generator import RandomNumbersGenerator, generate_random_rgb_color


class TestRandomNumbersGenerator(TestCase):
    def test_generate_random_rgb_color(self):
        color = generate_random_rgb_color()

        assert len(color) == 3
        assert all(x >= 0 for x in color)
        assert all(x <= 255 for x in color)

    def test_generate_random_pos(self):
        rng = RandomNumbersGenerator()

        pos = rng.generate_random_pos()
        assert len(pos) == 2

    def test_generate_two_random_pos(self):
        rng = RandomNumbersGenerator()

        pos_tup = rng.generate_two_random_pos()

        assert len(pos_tup) == 2
        assert len(pos_tup[0]) == 2
        assert len(pos_tup[1]) == 2
