import aggdraw
from PIL import Image
from LineArtTrainer.StraightLines import StraightLineGenerator
from LineArtTrainer.RandomCurvedLines import RandomCurvedLinesGenerator
from Scorer.ManhattenDistCalculator import ManhattanDistanceCalculator

def main() -> None:
    img = Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255)) # last part is image dimensions

    rclg = RandomCurvedLinesGenerator()
    rclg.draw_random_curved_lines(img, img)


    img_answer = Image.open("task.gif")
    rgb_img_answer = img_answer.convert('RGB')
    md_scorer = ManhattanDistanceCalculator()
    md_scorer.score_black_white(img, rgb_img_answer)

    #img.show()



if __name__ == "__main__":
    main()
