from Models.Web.exercise import Exercise


def saved_list_of_exercises() -> list:
    return [Exercise(
        "picture_url",
        "This is a description",
        "excercise_url",
        "3D Training"
    ), Exercise(
        "picture_url",
        "This is a description",
        "excercise_url",
        "Color Matching Training"
    ), Exercise(
        "picture_url",
        "This is a description",
        "excercise_url",
        "Light Shadow Training"
    ), Exercise(
        "picture_url",
        "This is a description",
        "excercise_url",
        "Line Art Training"
    )]


class DataRepository:
    def __init__(self) -> None:
        self.list_of_exercises = saved_list_of_exercises()

    def get_list_of_exercises(self) -> list:
        return self.list_of_exercises
