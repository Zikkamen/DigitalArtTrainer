from PIL import Image
from Trainers.LineArt.random_lines import RandomLines


class StraightLineGenerator:
    def __int__(self) -> None:
        pass

    def generate_random_straight_lines(self) -> None:
        img_task = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))
        img_task_view = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))
        img_answer = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))

        random_lines = RandomLines()
        random_lines.draw_random_lines(img_task, img_task_view, img_answer)

        img_task.save("Images/task.gif")
        img_task_view.save("Images/task_view.gif")
        img_answer.save("Images/answer.gif")