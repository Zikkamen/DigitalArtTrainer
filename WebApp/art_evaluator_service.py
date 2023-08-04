from PIL import Image

from WebApp.services.color_matcher_service import ColorMatcherService
from WebApp.persistence.data_service import DataService
from WebApp.persistence.file_service import FileService


def get_empty_canvas() -> Image:
    return Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))


class ArtEvaluatorService:
    def __init__(self) -> None:
        self.data_repo = DataService()
        #self.data_repo = None
        self.file_service = FileService()
        self.clm_service = ColorMatcherService()

    def get_list_of_exercises(self) -> list:
        return self.data_repo.get_list_of_exercises()

    def get_list_of_sub_exercises(self, exercise_name: str) -> list:
        return self.data_repo.get_list_of_sub_exercises(exercise_name)

    def get_file(self, exercise_id: int, file_name: str):
        return self.file_service.get_file(exercise_id, file_name)

    def get_filepath_of_dir(self, exercise_id: int) -> str:
        return self.file_service.get_directory_file_path(exercise_id)

    def generate_exercises(self, task: str, mode: str) -> int:
        print("Generating new Exercise")

        img_task = get_empty_canvas()

        if task == "ColorMatcher":
            return self.clm_service.generate_exercise(img_task, mode)

        return -1

    def submit_solution(self, exercise_id, img: Image) -> None:
        self.file_service.save_image(exercise_id, img, "solution.png")