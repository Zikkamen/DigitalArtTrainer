import numpy as np

from dataclasses import dataclass


@dataclass
class ColourMatcherScore:
    total_score: float
    single_scores: np.ndarray
