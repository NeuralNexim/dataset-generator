import multiprocessing as mp
from typing import Optional


def get_default_workers() -> int:
    """
    Default: all cores minus one, but at least 1.
    """
    try:
        count = mp.cpu_count()
    except NotImplementedError:
        return 1
    return max(1, count - 1)


def resolve_workers(user_workers: Optional[int]) -> int:
    if user_workers is not None and user_workers > 0:
        return user_workers
    return get_default_workers()
