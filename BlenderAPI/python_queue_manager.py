import os


class PythonQueueManager:
    def __init__(self):
        self.file_directory = os.path.dirname(__file__)
        self.python_file_queue_directory = os.path.join(self.file_directory, "PythonFileQueue")
        self.python_file_counter = 0


    def add_cube(self):
        pass