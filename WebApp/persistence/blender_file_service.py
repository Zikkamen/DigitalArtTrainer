import os
import glob
import re

import random

from PIL import Image


class BlenderFileService:
    def __init__(self):
        self.file_directory = os.path.dirname(__file__)
        self.file_directory_persistence = os.path.join(self.file_directory, "files")
        self.file_directory_blender_files = os.path.join(self.file_directory_persistence, "blender_files")

    def get_random_image(self, dir_name: str):
        file_path = random.choice(glob.glob(os.path.join(self.file_directory_blender_files, f"{dir_name}/*.png")))
        name = os.path.basename(file_path)

        im = Image.open(file_path)

        return im.convert("RGB"), re.findall("[xyz]", name), list(map(int, re.findall("[-0-9]+", name)))

    def get_zero_image_cube(self):
        im = Image.open(os.path.join(self.file_directory_blender_files, f"cube_z_rot/z_rot_0.png"))

        return im.convert('RGB')


if __name__ == "__main__":
    bfs = BlenderFileService()
    bfs.get_random_image("cube_x_y_z_rot")

    im = bfs.get_zero_image_cube()
    im.show()
