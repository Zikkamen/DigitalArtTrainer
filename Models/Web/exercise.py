from dataclasses import dataclass


@dataclass
class Exercise:
    exercise_name: str
    exercise_url: str
    picture_url: str
    description: str
