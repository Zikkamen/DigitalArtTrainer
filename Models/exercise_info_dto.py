from dataclasses import dataclass


@dataclass
class ExerciseInformationDto:
    id: int
    owner_id: str
    exercise_type: str
    sub_exercise_type: str
    creation_epoch: int
