import random
import numpy as np
from typing import Optional


def seed_everything(seed: Optional[int]):
    """
    Seed Python, NumPy, and any other RNGs for reproducibility.
    """
    if seed is None:
        return

    random.seed(seed)
    np.random.seed(seed)
