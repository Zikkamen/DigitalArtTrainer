from PIL import Image

from Trainers.ColorMatching.color_file_generator import ColorMatcherGenerator
from WebApp.persistence.file_service import FileService
from WebApp.persistence.data_service import DataService


class ColorMatcherService:
    def __init__(self) -> None:
        self.cmg = ColorMatcherGenerator()
        self.file_service = FileService()
        self.data_service = DataService()

    def generate_exercise(self, task_img: Image, mode: str) -> int:
        self.cmg.use_certain_number_generator(mode)
        answer = self.cmg.generate_file(task_img)

        exercise_id = self.file_service.generate_new_folder()
        self.file_service.save_image(exercise_id, task_img, "task_1.png")
        self.file_service.save_python_object(exercise_id, answer, "solution.dill")
        print(answer)

        return exercise_id
