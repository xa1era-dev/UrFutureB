from typing import List
from core.models.models import Course, Tag


# TODO: Заменить Course.lessons на Course.tags после внесения соответствующих правок в модель.
def get_course_weight(course: Course, tags: List[Tag], order_matters: bool = False) -> float:
    """
    Вычисляет вес курса как процент пересечения его тегов с указанными.

    Arguments:
        course -- объект Course, теги которого будут использоваться в вычислениях.
        tags -- список объектов Tag, перекрытие которых тегами курса мы будем высчитывать.

    Keyword Arguments:
        order_matters -- bool значение, определяющее значимость порядка следования тегов (default: False).

    Returns:
        Число типа float в диапазоне [0, 1].
    """
    return get_intersection_percentage([lesson.id for lesson in course.lessons], [tag.id for tag in tags]) / 100


def get_intersection_percentage(collection1: List, collection2: List) -> float:
    """
    Вычисляет процент покрытия второй коллекции первой.

    Arguments:
        collection1 -- первая коллекция.
        collection2 -- вторая коллекция, перекрытие которой первой мы будем высчитывать.

    Returns:
        Число типа float в диапазоне [0, 100].
    """
    return 100 * len(set(collection1) & set(collection2)) / len(collection2)
