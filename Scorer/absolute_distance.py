import numpy as np


class BitMaskCalculator:
    def __init__(self, penalty: float = 10, reward: float = 100) -> None:
        self.penalty = penalty
        self.reward = reward

    def bit_mask_scorer(self, img_submission, img_answer) -> float:
        np_submission = np.array(img_submission)
        np_answer = np.array(img_answer)

        np_diff = np.abs(np_submission - np_answer)
        np_score = (np_diff == 0) * self.reward - (np_diff > 0) * self.penalty

        return float(np.sum(np_score))
