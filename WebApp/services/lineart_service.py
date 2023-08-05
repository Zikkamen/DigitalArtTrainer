from PIL import Image

from Trainers.LineArt.random_curved_lines import RandomCurvedLinesGenerator
from Trainers.LineArt.straight_lines import StraightLineGenerator


class LineArtService:
    def __init__(self) -> None:
        self.line_art_generator_map = {
            'rclg': RandomCurvedLinesGenerator(),
            'rslg': StraightLineGenerator()
        }

    def generate_exercise(self, task_img: Image, mode: str) -> int:
        pass