from WebApp.persistence.data_repository import DataRepository


class ArtEvaluatorService:
    def __init__(self) -> None:
        self.data_repo = DataRepository()

    def get_list_of_exercises(self) -> list:
        return self.data_repo.get_list_of_exercises()
