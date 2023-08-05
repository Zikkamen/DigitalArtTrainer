from PIL import Image

from Models.Web.exercise_info import ExerciseInformation
from WebApp.services.color_matcher_service import ColorMatcherService
from WebApp.persistence.data_service import DataService
from WebApp.persistence.file_service import FileService
from WebApp.services.light_service import LightService
from WebApp.services.lineart_service import LineArtService
from WebApp.services.three_d_service import ThreeDService


def get_empty_canvas() -> Image:
    return Image.new(mode="RGB", size=(2480, 3580), color=(255, 255, 255))


class ArtEvaluatorService:
    def __init__(self) -> None:
        self.data_repo = DataService()
        self.file_service = FileService()
        self.service_map = {
            'ColorMatcher': ColorMatcherService(),
            'LineArt': LineArtService(),
            '3DRealm': ThreeDService(),
            'LightShadow': LightService()
        }

    def get_list_of_exercises(self) -> list:
        return self.data_repo.get_list_of_exercises()

    def get_list_of_sub_exercises(self, exercise_name: str) -> list:
        return self.data_repo.get_list_of_sub_exercises(exercise_name)

    def get_file(self, exercise_id: int, file_name: str):
        return self.file_service.get_filepath(exercise_id, file_name)

    def get_filepath_of_dir(self, exercise_id: int) -> str:
        return self.file_service.get_directory_file_path(exercise_id)

    def generate_exercises(self, task: str, mode: str) -> int:
        print("Generating new Exercise")

        img_task = get_empty_canvas()

        try:
            return self.service_map[task].generate_exercise(img_task, mode)
        except KeyError:
            return -1

    def get_exercise_info(self, exercise_id: int) -> ExerciseInformation:
        return self.data_repo.get_exercise_info(exercise_id)

    def store_submission(self, exercise_id: int, img: Image) -> None:
        self.file_service.save_image(exercise_id, img, "submission.png")
        self.data_repo.update_score(exercise_id, "In Progress")

    async def generate_score(self, exercise_id) -> None:
        extype, subextype, score = self.data_repo.get_exercise_and_subtype(exercise_id)

        self.service_map[extype].score_exercise(exercise_id, subextype)
