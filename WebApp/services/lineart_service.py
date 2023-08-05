import datetime
from asyncio import sleep

from PIL import Image

from Models.exercise_info_dto import ExerciseInformationDto
from Scorer.absolute_distance import BitMaskCalculator
from Scorer.manhatten_distance_calculator import ManhattanDistanceCalculator
from Trainers.LineArt.random_curved_lines import RandomCurvedLinesGenerator
from Trainers.LineArt.straight_lines import StraightLineGenerator
from WebApp.persistence.data_service import DataService
from WebApp.persistence.file_service import FileService


class LineArtService:
    def __init__(self) -> None:
        self.file_service = FileService()
        self.data_service = DataService()
        self.line_art_generator_map = {
            'randomcurvedlines': RandomCurvedLinesGenerator(),
            'randomstraightlines': StraightLineGenerator()
        }

        self.scorer_map = {
            'wo': BitMaskCalculator(),
            'woo': ManhattanDistanceCalculator()
        }

    def generate_exercise(self, task_img: Image, mode: str) -> int:
        mode_split = mode.split("_")

        answer_img = self.line_art_generator_map[mode_split[0]].generate_exercise(task_img)

        exercise_id = self.file_service.generate_new_folder()
        self.file_service.save_image(exercise_id, task_img, "task_1.png")
        self.file_service.save_image(exercise_id, answer_img, "solution.png")

        self.data_service.add_exercise_info(ExerciseInformationDto(
            exercise_id, "root", "LineArt", mode, int(datetime.datetime.now().timestamp())
        ))

        return exercise_id

    def score_exercise(self, exercise_id: int, subextype: str) -> None:
        sol_img_path = self.file_service.get_filepath(exercise_id, "solution.png")
        sub_img_path = self.file_service.get_filepath(exercise_id, "submission.png")

        sub_img = Image.open(sub_img_path)
        sub_img = sub_img.convert('RGB')
        sol_img = Image.open(sol_img_path)
        sol_img = sol_img.convert('RGB')

        mode_split = subextype.split("_")

        np_answer_bitmap = self.scorer_map[mode_split[1]].generate_bit_mask(sol_img)
        score = self.scorer_map[mode_split[1]].bit_mask_scorer(sub_img, np_answer_bitmap)

        self.data_service.update_score(exercise_id, f"Error Score: {score}")
        self.file_service.save_image(exercise_id, sol_img, "correction.png")

