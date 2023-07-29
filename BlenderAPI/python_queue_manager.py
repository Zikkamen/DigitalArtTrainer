import os
import re

from BlenderAPI.blender_api import BlenderApi


def set_position(original_str: str, position: tuple) -> str:
    original_str = re.sub("%x_pos", str(position[0]), original_str)
    original_str = re.sub("%y_pos", str(position[1]), original_str)
    original_str = re.sub("%z_pos", str(position[2]), original_str)

    return original_str


def set_rotation(original_str: str, rotation: tuple) -> str:
    original_str = re.sub("%x_rot", str(rotation[0]), original_str)
    original_str = re.sub("%y_rot", str(rotation[1]), original_str)
    original_str = re.sub("%z_rot", str(rotation[2]), original_str)

    return original_str


def set_feature(original_str: str, feature_name: str, value: float) -> str:
    original_str = re.sub(f"%{feature_name}", r'' + str(value), original_str)

    return original_str


class PythonQueueManager:
    def __init__(self):
        self.file_directory = os.path.dirname(__file__)
        self.python_file_queue_directory = os.path.join(self.file_directory, "BlenderPythonScripts")
        self.python_files_directory = os.path.join(self.file_directory, "PythonFiles")
        self.image_files_directory = os.path.join(self.file_directory, "Images")
        self.python_file_path = None
        self.python_file_counter = 0
        self.blender_api = BlenderApi("temp")

    def create_temp_pythonfile(self, file_name: str = "temp") -> None:
        with open(os.path.join(self.python_files_directory, "default.pyf"), "r") as fs:
            default_python_code = fs.read()

        self.python_file_path = os.path.join(self.python_file_queue_directory, f"{file_name}.py")

        with open(self.python_file_path, "w") as fs:
            fs.write(default_python_code)

    def add_cube(self, position: tuple, rotation: tuple, size: float) -> None:
        with open(os.path.join(self.python_files_directory, "add_cube.pyf")) as fs:
            cube_python_string = fs.read()

        cube_python_string = set_feature(cube_python_string, "size", size)
        cube_python_string = set_position(cube_python_string, position)
        cube_python_string = set_rotation(cube_python_string, rotation)

        self.write_to_python_file(cube_python_string)

    def add_point_light(self, position: tuple, energy: float) -> None:
        with open(os.path.join(self.python_files_directory, "add_point_light.pyf")) as fs:
            light_python_string = fs.read()

        light_python_string = set_feature(light_python_string, "energy", energy)
        light_python_string = set_position(light_python_string, position)

        self.write_to_python_file(light_python_string)

    def add_camera(self, position: tuple, rotation: tuple) -> None:
        with open(os.path.join(self.python_files_directory, "add_camera.pyf")) as fs:
            camera_python_string = fs.read()

        camera_python_string = set_position(camera_python_string, position)

        # Rotation in the plane where the axis is the normal. For exmaple the x determines the rotation in the y-z plane
        # Default setting at (0,0,0) the camera is pointed downwards to the x-y plane with the upper orientation facing positive y
        camera_python_string = set_rotation(camera_python_string, rotation)

        self.write_to_python_file(camera_python_string)

    def render_blender_image(self, filename: str = "temp.png") -> None:
        with open(os.path.join(self.python_files_directory, "render_image.pyf")) as fs:
            render_python_string = fs.read()

        render_python_string = render_python_string.replace("%file_path", rf'r"{os.path.join(self.image_files_directory, filename)}"')

        self.write_to_python_file(render_python_string)

    def save_file(self) -> None:
        self.write_to_python_file("bpy.ops.wm.save_mainfile()")

    def write_to_python_file(self, content: str) -> None:
        with open(self.python_file_path, "a") as fs:
            fs.write(content + "\n")

    def create_new_blender_file_and_execute(self, file_name: str = "cube_on_plane") -> None:
        self.blender_api.new_temp_file(file_name)

        print(self.python_file_path)
        self.blender_api.run_blender_command(self.python_file_path)


if __name__ == "__main__":
    python_queue_manager = PythonQueueManager()
    python_queue_manager.create_temp_pythonfile()
    python_queue_manager.add_cube((0, 0, 0), (0, 45, 0), 1)
    # python_queue_manager.add_point_light((4, 1, 6), 1000)
    python_queue_manager.add_camera((0, 0, 5), (0, 0, 0))
    python_queue_manager.render_blender_image()
    python_queue_manager.save_file()

    python_queue_manager.create_new_blender_file_and_execute("empty")
