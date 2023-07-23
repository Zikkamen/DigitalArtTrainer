import shutil
import os


class BlenderApi:
    def __init__(self) -> None:
        self.file_directory = os.path.dirname(__file__)
        self.blender_files_output_directory = os.path.join(self.file_directory, "BlenderOutputFiles")
        self.blender_template_files_directory = os.path.join(self.file_directory, "BlenderTemplates")
        self.python_file_queue_directory = os.path.join(self.file_directory, "BlenderPythonScripts")
        self.output_blender_file_path = os.path.join(self.blender_files_output_directory, "temp.blend")

    def new_temp_file(self) -> None:
        shutil.copy(
            os.path.join(self.blender_template_files_directory, "cube_on_plane.blend"),
            self.output_blender_file_path
        )

    def set_file_name(self, file_name: str) -> None:
        self.output_blender_file_path = os.path.join(self.blender_files_output_directory, f"{file_name}.blend")

    def delete_temp_file(self) -> None:
        if not os.path.exists(self.output_blender_file_path):
            return

        os.remove(self.output_blender_file_path)

    def run_blender_command(self, instruction: str) -> None:
        temp_python_file_path = os.path.join(self.python_file_queue_directory, f"{instruction}.py")

        command = f'blender {self.output_blender_file_path} -b -P {temp_python_file_path}'

        os.system(command)


if __name__ == "__main__":
    blender_api = BlenderApi()
    blender_api.new_temp_file()
    blender_api.run_blender_command()
