import datetime
import os

from PIL import Image, ImageDraw, ImageFont

from Models.exercise_info_dto import ExerciseInformationDto
from Scorer.absolute_distance import BitMaskCalculator
from WebApp.persistence.blender_file_service import BlenderFileService
from WebApp.persistence.data_service import DataService
from WebApp.persistence.file_service import FileService


class ThreeDService:
    def __init__(self):
        self.blender_file_service = BlenderFileService()
        self.file_service = FileService()
        self.data_service = DataService()
        self.scorer_service = BitMaskCalculator()
        self.font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "../../Arial.ttf"), 75)
        self.coord_map = {
            'x': 'down',
            'y': 'right',
            'z': 'counter clockw'
        }

    def generate_exercise(self, task_img: Image, mode: str) -> int:
        answer_img, coords, val = self.blender_file_service.get_random_image(mode)
        task_img = self.blender_file_service.get_zero_image_cube()
        draw_task = ImageDraw.Draw(task_img)
        empty_img = Image.new(mode="RGB", size=answer_img.size, color=(71, 71, 71))

        for i in range(len(coords)):
            draw_task.text((10, i * 100), f"{self.coord_map[coords[i]]}: {val[i]}", (255, 255, 255), self.font)

        exercise_id = self.file_service.generate_new_folder()
        self.file_service.save_image(exercise_id, task_img, "task_1.png")
        self.file_service.save_image(exercise_id, empty_img, "empty.png")
        self.file_service.save_image(exercise_id, answer_img, "solution.png")

        self.data_service.add_exercise_info(ExerciseInformationDto(
            exercise_id, "root", "3DRealm", mode, int(datetime.datetime.now().timestamp())
        ))

        return exercise_id

    def score_exercise(self, exercise_id: int, subextype: str) -> None:
        sol_file_path = self.file_service.get_filepath(exercise_id, "solution.png")
        sub_img_path = self.file_service.get_filepath(exercise_id, "submission.png")

        sub_img = Image.open(sub_img_path)
        sub_img = sub_img.convert('RGB')
        sol_img = Image.open(sol_file_path)
        sol_img = sol_img.convert('RGB')

        score = self.scorer_service.get_bit_mask_score(sub_img, sol_img)
        self.file_service.save_image(exercise_id, sol_img, "correction.png")
        self.data_service.update_score(exercise_id, f"Error Score: {score}")


if __name__ == "__main__":
    tds = ThreeDService()
    tds.generate_exercise(None, "cube_x_y_z_rot")