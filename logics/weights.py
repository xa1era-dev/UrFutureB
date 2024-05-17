from typing import List, Tuple, Set
from core import Course, Tag, Competence, Profession


def get_course_weight(course: Course, tags: List[Tag], order_matters: bool = False) -> float:
    """
    Вычисляет вес курса, как процент покрытия указанных тегов его тегами.

    Arguments:
        course -- объект Course, теги которого будут использоваться в вычислениях.
        tags -- список объектов Tag, перекрытие которых тегами курса мы будем высчитывать.

    Keyword Arguments:
        order_matters -- bool значение, определяющее значимость порядка следования тегов (default: False).

    Returns:
        Число типа float в диапазоне [0, 1].
    """
    return get_overlapping_percentage(course.tags, tags) / 100


def get_overlapping_percentage(collection1: List, collection2: List) -> float:
    """
    Вычисляет процент покрытия второй коллекции первой.

    Arguments:
        collection1 -- первая коллекция.
        collection2 -- вторая коллекция, перекрытие которой первой мы будем высчитывать.

    Returns:
        Число типа float в диапазоне [0, 100].
    """
    coll2_len = len(collection2)

    if coll2_len == 0:
        return 0.0

    return 100 * len(set(collection1) & set(collection2)) / coll2_len
