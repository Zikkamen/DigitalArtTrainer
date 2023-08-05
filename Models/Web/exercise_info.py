from dataclasses import dataclass


@dataclass
class ExerciseInformation:
    exercise_name: str
    tasks_list: list
    exercise_description: str
    score: str
