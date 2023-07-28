import numpy as np

from Models.colour_matcher_score import ColourMatcherScore


def penalty_linear(np_diff: np.ndarray) -> np.ndarray:
    return np_diff


def penalty_quadratic(np_diff: np.ndarray) -> np.ndarray:
    return np.power(np_diff, 2)


class ColorMatcherScorer:
    def __init__(self, penalty_string: str = "linear") -> None:
        self.penalty_function_map = {
            'linear': penalty_linear,
            'quadratic': penalty_quadratic
        }

        self.penalty_function = self.penalty_function_map[penalty_string]

    def calculate_difference(self, np_submission: np.ndarray, np_answer: np.ndarray) -> ColourMatcherScore:
        np_difference = np.abs(np_answer - np_submission)
        np_single_scores = np.sum(self.penalty_function(np_difference), axis=1)

        return ColourMatcherScore(float(np.sum(np_single_scores)), np_single_scores)


if __name__ == "__main__":
    color_score = ColorMatcherScorer("quadratic")

    submission = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    answer = submission + 3

    print(color_score.calculate_difference(submission, answer))
