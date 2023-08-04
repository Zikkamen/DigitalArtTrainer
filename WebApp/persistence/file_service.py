import glob
import os.path
import random


from PIL import Image
from dill import dumps, loads


def generate_random_id() -> int:
    return random.randint(0, 9223372036854775807)


class FileService:
    def __init__(self) -> None:
        self.file_directory = os.path.dirname(__file__)
        self.file_directory_persistence = os.path.join(self.file_directory, "files")
        self.file_directory_exercise = os.path.join(self.file_directory_persistence, "exercise")

    def get_file(self, exercise_id: int, file_name: str) -> str:
        cur_file = os.path.join(self.file_directory_exercise, f"{exercise_id}/{file_name}")

        if not os.path.exists(cur_file):
            return None

        return cur_file

    def create_new_exercise_folder(self, exercise_id: int) -> bool:
        new_dir = os.path.join(self.file_directory_exercise, str(exercise_id))

        if os.path.isdir(new_dir):
            return False

        os.mkdir(new_dir)
        return True

    def save_image(self, exercise_id: int, img: Image, img_name: str) -> None:
        cur_dir = os.path.join(self.file_directory_exercise, str(exercise_id))

        img.save(os.path.join(cur_dir, img_name))

    def save_python_object(self, exercise_id: int, obj: object, obj_name: str) -> None:
        cur_dir = os.path.join(self.file_directory_exercise, str(exercise_id))

        with open(os.path.join(cur_dir, obj_name), "wb") as fs:
            fs.write(dumps(obj))

    def remove_directory(self, exercise_id: int) -> None:
        cur_dir = self.get_directory_file_path(exercise_id)
        os.rmdir(cur_dir)

    def generate_new_folder(self) -> int:
        exercise_id = -1

        for i in range(10):
            exercise_id = generate_random_id()

            if self.create_new_exercise_folder(exercise_id):
                break

        return exercise_id

    def get_directory_file_path(self, exercise_id) -> str:
        cur_dir = os.path.join(self.file_directory_exercise, str(exercise_id))

        if os.path.isdir(cur_dir):
            return cur_dir

        return None
