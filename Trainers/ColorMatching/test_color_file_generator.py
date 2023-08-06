from unittest import TestCase

from Trainers.ColorMatching.color_file_generator import *


class TestDarknessColorGenerator(TestCase):
    def test_generate_darkness_color(self):
        numbers = generate_uniform_random_numbers()

        assert len(numbers) == 3
        assert all(x >= 0 for x in numbers)
        assert all(x <= 255 for x in numbers)

    def test_set_first_datapoint(self):
        numbers = generate_hue_random_number()

        assert len(numbers) == 3
        assert min(numbers) == 0
        assert max(numbers) == 255
        assert all(x >= 0 for x in numbers)
        assert all(x <= 255 for x in numbers)

    def test_generate_darkness_color_gen(self):
        dcg = DarknessColorGenerator()

        color = dcg.generate_darkness_color()

        assert len(color) == 3
        assert all(x >= 0 for x in color)
        assert all(x <= 255 for x in color)

    def test_generate_saturation_color(self):
        scg = SaturationColorGenerator()

        color = scg.generate_saturation_color()

        assert len(color) == 3
        assert all(x >= 0 for x in color)
        assert all(x <= 255 for x in color)

    def test_saturation_and_darken_color(self):
        scg = DarknessColorGenerator()

        color = scg.generate_darkness_color()

        assert len(color) == 3
        assert all(x >= 0 for x in color)
        assert all(x <= 255 for x in color)

    def test_generate_exercise(self):
        im = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))
        cmg = ColorMatcherGenerator()
        answer = cmg.generate_exercise(im)

        assert len(answer) == 45