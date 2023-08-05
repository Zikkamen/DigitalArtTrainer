from PIL import Image
from Trainers.LineArt.random_lines import RandomLines


class StraightLineGenerator:
    def __int__(self) -> None:
        self.random_lines_generator = RandomLines()

    def generate_exercise(self, img_task: Image) -> Image:
        img_answer = Image.new(mode="RGB", size=img_task.size, color=(255, 255, 255))

        self.random_lines_generator.draw_random_lines(img_task, img_answer)

        return img_answer
