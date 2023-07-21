from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class ManhattanDistanceCalculator:
    def __init__(self) -> None:
        pass

    def score_black_white(self, img_submission : Image, img_answer : Image) -> float:
        np_submission = np.array(img_submission)
        np_answer = np.array(img_answer)

        print(np_answer.shape)

        np_answer_sum_colors = np.sum(img_answer, axis=2)
        np_answer_sum_colors_bitmap = np_answer_sum_colors < 750

        np_answer_shape = np_answer_sum_colors_bitmap.shape
        np_answer_md = np.full(np_answer_shape, np.inf)

        for i in range(np_answer_shape[1]):
            lowest_num = np.inf

            for j in range(np_answer_shape[0]):
                if np_answer_sum_colors_bitmap[j,i]:
                    lowest_num = 0

                np_answer_md[j,i] = min(np_answer_md[j,i], lowest_num)
                lowest_num += 1

        for i in range(np_answer_shape[1]):
            lowest_num = np.inf

            for j in range(np_answer_shape[0] - 1, -1, -1):
                if np_answer_sum_colors_bitmap[j,i]:
                    lowest_num = 0

                np_answer_md[j,i] = min(np_answer_md[j,i], lowest_num)
                lowest_num += 1

        for j in range(np_answer_shape[0]):
            lowest_num = np.inf

            for i in range(np_answer_shape[1]):
                lowest_num = min(lowest_num, np_answer_md[j, i])
                np_answer_md[j,i] = min(np_answer_md[j,i], lowest_num)
                lowest_num += 1

        for j in range(np_answer_shape[0]):
            lowest_num = np.inf

            for i in range(np_answer_shape[1] - 1, -1, -1):
                lowest_num = min(lowest_num, np_answer_md[j,i])
                np_answer_md[j,i] = min(np_answer_md[j,i], lowest_num)
                lowest_num += 1

        print(np_answer_md)
        img_answer.show()

        plt.imshow(np_answer_md, cmap='hot', interpolation='nearest')
        plt.show()
