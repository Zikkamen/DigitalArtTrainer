from unittest import TestCase
from mock import patch

from python_queue_manager import *


class Test(TestCase):
    def test_set_position(self):
        test_string = "%x_pos, %y_pos, %z_pos"

        replaced_string = set_position(test_string, (1, 2, 3))

        assert replaced_string == "1, 2, 3"

    def test_set_rotation(self):
        test_string = "%x_rot, %y_rot, %z_rot"

        replaced_string = set_rotation(test_string, (1, 2, 3))

        assert replaced_string == "1, 2, 3"

    def test_set_featuren(self):
        test_string = "size=%feature"

        replaced_string = set_feature(test_string, "feature", 1)

        assert replaced_string == "size=1"
