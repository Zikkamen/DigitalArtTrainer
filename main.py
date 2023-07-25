from PIL import Image

from Scorer.manhatten_distance_calculator import ManhattanDistanceCalculator
from Trainers.LineArt.straight_lines import StraightLineGenerator
from Trainers.LineArt.random_curved_lines import RandomCurvedLinesGenerator


def main() -> None:
    img = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255)) # last part is image dimensions


    slg = StraightLineGenerator()
    slg.generate_random_straight_lines()

    rclg = RandomCurvedLinesGenerator()
    rclg.draw_random_curved_lines(img, img)

    img.show()


    img_answer = Image.open("Images/task.gif")
    rgb_img_answer = img_answer.convert('RGB')
    md_scorer = ManhattanDistanceCalculator()
    md_scorer.score_black_white(img, rgb_img_answer)

    img.show()


if __name__ == "__main__":
    main()
