import numpy as np
import copy

from unittest import TestCase

from Scorer.absolute_distance import BitMaskCalculator


class TestBitMaskCalculator(TestCase):
    def test_bit_mask_scorer_all_correct(self):
        bmc = BitMaskCalculator()

        rand_array = np.random.randint(0, 1, (10, 10))

        assert bmc.bit_mask_scorer(rand_array, rand_array) == 10 * 10 * bmc.reward

    def test_bit_mask_scorer_all_wrong(self):
        bmc = BitMaskCalculator()

        rand_array = np.random.randint(0, 1, (10, 10))

        assert bmc.bit_mask_scorer(rand_array, rand_array == 0) == - 10 * 10 * bmc.penalty

    def test_bit_mask_scorer(self):
        bmc = BitMaskCalculator()

        rand_array = np.ones((10, 10))
        rand_array_new = copy.deepcopy(rand_array)
        rand_array_new[0] = np.zeros((1, 10))

        assert bmc.bit_mask_scorer(rand_array, rand_array_new == 0)\
               == 10 * bmc.reward - 9 * 10 * bmc.penalty