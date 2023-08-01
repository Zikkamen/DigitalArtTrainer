from WebApp.persistence.data_service import DataService


class ArtEvaluatorService:
    def __init__(self) -> None:
        self.data_repo = DataService()

    def get_list_of_exercises(self) -> list:
        return self.data_repo.get_list_of_exercises()

    def get_list_of_subexercises(self, exercise_name: str) -> list:
        return self.data_repo.get_list_of_subexercises(exercise_name)
