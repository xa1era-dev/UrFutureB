from typing import List, Tuple, Set

from core import Course, Tag, Profession, Competence
from logics import get_course_weight, get_overlapping_percentage


# Ожидается, что в метод поступят компетенции, теги которых уже совпадают с тегами выбранной професии.
# Слой корневой бизнес-логики не должен зависить от слоя доступа к данным, поэтому я считаю, что будет
# некорректно в этом методе использовать какие-либо sql-выборки (orm-операции).
# Таким образом, на более высоком уровне (слое) нужно получить связанные с профессией компетенции
# по тегам профессии и только потом вызвать этот метод с полученным множеством компетенций.
def get_sorted_competences_and_all_tags(
        profession: Profession,
        competences: List[Competence],
        descending: bool = True) -> Tuple[List[Competence], Set[Tag]]:
    """
    Сортирует множество компетенций на основании покрытия тегов професии их тегами.
    Создаёт множество всех тегов переданных компетенций без повторений.

    Arguments:
        profession -- объект Profession выбранной професии.
        competences -- список объектов Competence, у которых хотя бы один тег пересекается с тегами профессии.

    Keyword Arguments:
        descending -- нужна ли сортировка в обратном порядке.

    Returns:
        Кортеж из двух значений: (list(сортированные компетенции); set(объединение всех тегов компетенций)).
    """
    competences.sort(key=lambda comp: get_overlapping_percentage(comp.tags, profession.tags), reverse=descending)
    all_tags = {item for competence in competences for item in competence.tags}

    return competences, all_tags


def get_courses_sorted_by_relevance(
        courses: List[Course],
        tags_lists: List[List[Tag]],
        descending: bool = True) -> List[Course]:
    """
    Сортирует множество курсов на основании средней релевантности каждого курса.

    Arguments:
        courses -- список объектов Course.
        tags_lists -- список списков объектов Tag.

    Keyword Arguments:
        descending -- нужна ли сортировка по убыванию.

    Returns:
        Сортированный по средней релевантности список объектов Course.
    """
    courses.sort(key=lambda course: get_course_average_relevance(course, tags_lists), reverse=descending)
    return courses


def get_course_average_relevance(
        course: Course,
        tags_list: List[List[Tag]]) -> float:
    """
    Вычисляет среднюю релевантность курса как среднее значение по покрытию каждого списка тегов тегами курса.

    Arguments:
        course -- объект Course, для которого будем считать среднюю релевантность.
        tags_list -- список списков объектов Tag.

    Returns:
        Среднее значение релевантности типа float в диапазоне [0, 1].
    """
    count, relevance = len(tags_list), 0

    for tag_list in tags_list:
        relevance += get_course_weight(course, tag_list)

    return relevance / count if count > 0 else 0.0
