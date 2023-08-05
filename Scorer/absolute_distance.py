import numpy as np
from PIL import Image


class BitMaskCalculator:
    def __init__(self, penalty: float = 10, reward: float = 100) -> None:
        self.penalty = penalty
        self.reward = reward

    def bit_mask_scorer(self, img_submission: Image, np_answer: np.array) -> float:
        np_submission = np.sum(np.array(img_submission), axis=2) >= 150
        np_diff = np_submission != np_answer

        return np.sum(np_diff * self.penalty) + max(0, np.sum(np_submission) - np.sum(np_answer)) / 100

    def generate_bit_mask(self, img_answer: Image) -> np.array:
        np_answer_matrix = np.array(img_answer)
        np_answer_sum_colors = np.sum(np_answer_matrix, axis=2)
        np_answer_sum_colors_bitmap = np_answer_sum_colors >= 150

        return np_answer_sum_colors_bitmap

    def get_bit_mask_score(self, img_submission: Image, img_answer: Image) -> float:
        np_answer = np.array(img_answer)
        np_submission = np.array(img_submission)

        np_answer_sum = np.sum(np_answer, axis=2)
        np_submission_sum = np.sum(np_submission, axis=2)

        np_ans_mask_g = np_answer_sum > 3 * 69
        np_ans_mask_l = np_answer_sum < 3 * 72
        np_ans_mask = np_ans_mask_g * np_ans_mask_l

        np_sub_mask_g = np_submission_sum > 3 * 69
        np_sun_mask_l = np_submission_sum < 3 * 72
        np_sub_mask = np_sub_mask_g * np_sun_mask_l

        np_diff = np_ans_mask != np_sub_mask

        return float(np.sum(np_diff))
