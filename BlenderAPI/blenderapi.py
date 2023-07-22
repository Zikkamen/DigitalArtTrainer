import shutil
import os


class BlenderApi:
    def __init__(self) -> None:
        self.file_directory = os.path.dirname(__file__)
        self.blender_files_directory = os.path.join(self.file_directory, "BlenderFiles")
        self.temp_blender_file_path = os.path.join(self.blender_files_directory, "temp.blend")
        self.temp_python_file_path = os.path.join(self.blender_files_directory, "temp.py")

    def new_temp_file(self) -> None:
        shutil.copy(
            os.path.join(self.blender_files_directory, "template.blend"),
            self.temp_blender_file_path
        )

    def delete_temp_file(self) -> None:
        if not os.path.exists(self.temp_blender_file_path):
            return

        os.remove(self.temp_blender_file_path)

    def run_blender_command(self) -> None:
        command = f'blender {self.temp_blender_file_path} -b -P {self.temp_python_file_path}'

        #with open(self.temp_python_file_path, "w") as fs:
            #fs.write("import bpy\nprint(bpy.data.filepath)")

        os.system(command)


if __name__ == "__main__":
    blender_api = BlenderApi()
    blender_api.new_temp_file()
    blender_api.run_blender_command()
