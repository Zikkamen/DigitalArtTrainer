import datetime

from PIL import Image
from dill import loads

from Models.exercise_info_dto import ExerciseInformationDto
from Scorer.color_matcher_difference import ColorMatcherScorer
from Trainers.ColorMatching.color_file_generator import ColorMatcherGenerator
from WebApp.persistence.file_service import FileService
from WebApp.persistence.data_service import DataService


class ColorMatcherService:
    def __init__(self) -> None:
        self.cmg = ColorMatcherGenerator()
        self.file_service = FileService()
        self.data_service = DataService()
        self.scorer_service = ColorMatcherScorer()

    def generate_exercise(self, task_img: Image, mode: str) -> int:
        self.cmg.use_certain_number_generator(mode)
        answer = self.cmg.generate_exercise(task_img)

        exercise_id = self.file_service.generate_new_folder()
        self.file_service.save_image(exercise_id, task_img, "task_1.png")
        self.file_service.save_python_object(exercise_id, answer, "solution.dill")

        self.data_service.add_exercise_info(ExerciseInformationDto(
            exercise_id, "root", "ColorMatcher", mode, int(datetime.datetime.now().timestamp())
        ))

        return exercise_id

    def score_exercise(self, exercise_id: int, subextype: str) -> None:
        sol_file_path = self.file_service.get_filepath(exercise_id, "solution.dill")
        sub_img_path = self.file_service.get_filepath(exercise_id, "submission.png")

        with open(sol_file_path, "rb") as fs:
            sol_file = loads(fs.read())

        sub_img = Image.open(sub_img_path)
        sub_img = sub_img.convert('RGB')

        cms = self.scorer_service.score_files(sol_file, sub_img)
        self.cmg.write_score_card(sub_img, cms.single_scores)
        self.file_service.save_image(exercise_id, sub_img, "correction.png")
        self.data_service.update_score(exercise_id, f"Error Score: {cms.total_score}")
