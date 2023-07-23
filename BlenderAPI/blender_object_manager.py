from python_queue_manager import PythonQueueManager


class BlenderObjectManager:
    def __init__(self):
        self.python_queue_manager = PythonQueueManager()

    def add_cube(self):
        self.python_queue_manager.add_cube()
