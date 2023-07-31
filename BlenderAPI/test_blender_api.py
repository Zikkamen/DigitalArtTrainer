from unittest import TestCase
from mock import patch

from BlenderAPI.blender_api import BlenderApi


class TestBlenderApi(TestCase):
    def mock_copy(self):
        return

    @patch('shutil.copy')
    def test_new_temp_file(self, MockClass1):
        blender_api = BlenderApi()
        blender_api.new_temp_file()

        assert MockClass1.called

    @patch('os.remove')
    @patch('os.path')
    def test_delete_temp_file_not_exists(self, MockClass1, MockClass2):
        MockClass2.exists.return_value = False

        blender_api = BlenderApi()
        blender_api.delete_temp_file()

        assert not MockClass1.called

    @patch('os.remove')
    @patch('os.path.exists')
    def test_delete_temp_file_exists(self, MockClass1, MockClass2):
        MockClass2.return_value = True

        blender_api = BlenderApi()
        blender_api.delete_temp_file()

        assert MockClass1.called

    @patch('os.system')
    def test_run_blender_command(self, MockClass1):
        blender_api = BlenderApi()
        blender_api.run_blender_command("temp")

        assert MockClass1.called
