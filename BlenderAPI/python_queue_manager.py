import os
import re

class PythonQueueManager:
    def __init__(self):
        self.file_directory = os.path.dirname(__file__)
        self.python_file_queue_directory = os.path.join(self.file_directory, "BlenderPythonScripts")
        self.python_files_directory = os.path.join(self.file_directory, "PythonFiles")
        self.python_file_path = None
        self.python_file_counter = 0

    def create_temp_pythonfile(self, file_name: str = "temp") -> None:
        with open(os.path.join(self.python_files_directory, "default.pyf"), "r") as fs:
            default_python_code = fs.read()

        self.python_file_path = os.path.join(self.python_file_queue_directory, f"{file_name}.py")

        with open(self.python_file_path, "w") as fs:
            fs.write(default_python_code)

    def add_cube(self, position: tuple, size: float) -> None:
        with open(os.path.join(self.python_files_directory, "add_cube.pyf")) as fs:
            cube_python_string = fs.read()

        cube_python_string = re.sub("%size", str(size), cube_python_string)
        cube_python_string = re.sub("%x_pos", str(position[0]), cube_python_string)
        cube_python_string = re.sub("%y_pos", str(position[1]), cube_python_string)
        cube_python_string = re.sub("%z_pos", str(position[2]), cube_python_string)

        self.write_to_python_file(cube_python_string)

    def save_file(self) -> None:
        self.write_to_python_file("bpy.ops.wm.save_mainfile()")

    def write_to_python_file(self, content: str) -> None:
        with open(self.python_file_path, "a") as fs:
            fs.write(content + "\n")


if __name__ == "__main__":
    python_queue_manager = PythonQueueManager()
    python_queue_manager.create_temp_pythonfile()
    python_queue_manager.add_cube((1, 2, 3), 4)
    python_queue_manager.save_file()
