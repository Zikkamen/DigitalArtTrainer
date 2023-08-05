import numpy as np

from PIL import Image


class ManhattanDistanceCalculator:
    def __init__(self) -> None:
        self.np_answer_md = None
        self.np_answer_matrix = None
        self.np_answer_sum_colors_bitmap = None

    def iterate_through_matrix_x(self, start: int, end: int, step: int, matrix_shape: tuple) -> None:
        for i in range(matrix_shape[1]):
            lowest_num = np.inf

            for j in range(start, end, step):
                if self.np_answer_sum_colors_bitmap[j,i]:
                    lowest_num = 0

                self.np_answer_md[j, i] = min(self.np_answer_md[j, i], lowest_num)
                lowest_num += 1

    def iterate_through_matrix_y(self, start: int, end: int, step: int, matrix_shape: tuple) -> None:
        for j in range(matrix_shape[0]):
            lowest_num = np.inf

            for i in range(start, end, step):
                lowest_num = min(lowest_num, self.np_answer_md[j, i])
                self.np_answer_md[j, i] = min(self.np_answer_md[j, i], lowest_num)
                lowest_num += 1

    def generate_bit_mask(self, img_answer: Image) -> np.array:
        self.np_answer_matrix = np.array(img_answer)

        np_answer_sum_colors = np.sum(img_answer, axis=2)
        self.np_answer_sum_colors_bitmap = np_answer_sum_colors < 750

        np_answer_shape = self.np_answer_sum_colors_bitmap.shape
        self.np_answer_md = np.full(np_answer_shape, np.inf)

        self.iterate_through_matrix_x(0, np_answer_shape[0], 1, np_answer_shape)
        self.iterate_through_matrix_x(np_answer_shape[0] - 1, -1, -1, np_answer_shape)
        self.iterate_through_matrix_y(0, np_answer_shape[1], 1, np_answer_shape)
        self.iterate_through_matrix_y(np_answer_shape[1] - 1, -1, -1, np_answer_shape)

        return self.np_answer_md

    def bit_mask_scorer(self, img_submission: Image, np_answer: np.array) -> float:
        np_submission = np.sum(np.array(img_submission), axis=2) <= 615
        np_diff = np_submission * np_answer

        return np.sum(np_diff * 10) + max(0, np.sum(np_submission) - np.sum(np_answer == 0)) / 100