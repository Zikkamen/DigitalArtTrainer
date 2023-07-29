from dataclasses import dataclass


@dataclass
class Exercise:
    picture_url: str
    description: str
    exercise_url: str
    exercise_name: str
