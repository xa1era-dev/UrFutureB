from itertools import chain
from typing import List, Set
from core.models import Course, Tag, Profession, Competence
from .weights import get_course_weight, get_overlapping_percentage


def sort_competences_by_intersection_with_profession_tags(
        profession: Profession,
        competences: List[Competence],
        descending: bool = True) -> None:
    """
    Сортирует множество компетенций на основании покрытия тегов професии их тегами.

    Arguments:
        profession -- объект Profession выбранной професии.
        competences -- список объектов Competence, у которых хотя бы один тег пересекается с тегами профессии.

    Keyword Arguments:
        descending -- нужна ли сортировка в обратном порядке.
    """
    competences.sort(key=lambda comp: get_overlapping_percentage(comp.tags, profession.tags), reverse=descending)


def get_courses_sorted_by_relevance(
        courses: List[Course],
        competences: List[Competence],
        descending: bool = True,
        remove_zeros: bool = False) -> List[Course]:
    """
    Сортирует множество курсов на основании средней релевантности каждого курса.
    Удаляет курсы с нулевой релевантностью, если требуется.

    Arguments:
        courses -- список объектов Course.
        competences -- список объектов Competence.

    Keyword Arguments:
        descending -- нужна ли сортировка по убыванию.
        remove_zeros -- нужно ли удалять курсы с нулевой релевантностью.

    Returns:
        Упорядоченный список объектов Course.
    """
    comp_tags = [comp.tags for comp in competences]

    result_courses = list()
    relevants = dict()

    for crs in courses:
        relevants[crs.id] = get_course_average_relevance(crs, comp_tags)

    for crs in courses:
        if relevants[crs.id] == 0 and remove_zeros:
            continue

        result_courses.append(crs)

    result_courses.sort(key=lambda c: relevants[c.id], reverse=descending)
    return result_courses


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


def get_all_tags(competences: List[Competence]) -> Set[Tag]:
    """
    Формирует и возвращает общее множество уникальных тегов переданных компетенций.

    Arguments:
        competences -- список объектов Competence.

    Returns:
        Множество уникальных тегов.
    """
    return set(chain.from_iterable(comp.tags for comp in competences))
