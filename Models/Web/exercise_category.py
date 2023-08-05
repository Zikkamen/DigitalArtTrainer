from dataclasses import dataclass


@dataclass
class ExerciseCategory:
    exercise_name: str
    exercise_url: str
    picture_url: str
    description: str
