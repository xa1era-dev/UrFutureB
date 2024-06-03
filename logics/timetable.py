from typing import List, Dict, Tuple

# TODO: Перейти на использование моделей, вместо схем.
from schemas.group import Group
from schemas.discipline import Discipline

from core import Competence, LessonTimeChoice, TeacherChoice, Course

from logics.timetable_builder import Timetable
from sorting import get_courses_sorted_by_relevance
from logics.constants import *


def build_timetable(
        compteneces: List[Competence],
        disciplines: List[Discipline],
        preferred_times: List[LessonTimeChoice],
        preferred_teachers: Dict[int, List[TeacherChoice]],
        preferred_courses: Dict[int, List[Course]]) -> Dict[int, Tuple[Course, Group]]:
    # Сортируем курсы каждой дисциплины, чтобы наиболее подходящие для выбранной профессии были в начале списка.
    # (профессия представлена в виде набора связанных с ней компетенций).
    # Удаляем курсы, которые абсолютно не подходят для выбранной профессии.
    for discipline in disciplines:
        discipline.courses = get_courses_sorted_by_relevance(discipline.courses, compteneces, remove_zeros=True)

    # Группируем интервалы по дням для ускорения поиска временных интервалов.
    grouped_times = get_times_grouped_by_day(preferred_times)

    for discipline in disciplines:
        # Формируем коэффициенты для избранных преподавателей.
        preferred_teachers_coeffs = get_preffered_teachers_coefficients(preferred_teachers.get(discipline.id, []))

        # Сортируем группы каждого курса, включая приоритетные (курсы) для пользователя.
        sort_courses_groups(discipline.courses, grouped_times, preferred_teachers_coeffs)
        sort_courses_groups(preferred_courses.get(discipline.id, []), grouped_times, preferred_teachers_coeffs)

    timetable = Timetable(week_length=7, classes_at_day=10)
    final_selection = dict()

    for discipline in disciplines:
        preferred = preferred_courses.get(discipline.id, None)
        course_with_group = None

        if preferred is not None:
            course_with_group = try_choose_group(preferred, timetable)

        if course_with_group is None:
            course_with_group = try_choose_group(discipline.courses, timetable)

        if course_with_group is None:
            raise Exception("Something went wrong: must be at least 1 (course, group) pair.")

        final_selection[discipline.id] = (course_with_group[0], course_with_group[1])

    return final_selection


def try_choose_group(courses: List[Course], timetable: Timetable) -> tuple[Course, Group] | None:
    for course in courses:
        for group in course.groups:
            time_fit = True

            for lesson in group.lessons:
                time_fit &= timetable.can_add(lesson.day, lesson.start, lesson.end)

            if time_fit:
                for lesson in group.lessons:
                    timetable.add_without_validation(lesson.day, lesson.start, lesson.end)

                return course, group

    return None


def sort_courses_groups(
        courses: List[Course],
        grouped_times: Dict[int, List[LessonTimeChoice]],
        teachers_coeffs: Dict[int, float]) -> None:
    for course in courses:
        groups_weights = dict()

        for group in course.groups:
            groups_weights[group.uuid_] = \
                (get_time_coefficient(group, grouped_times) * get_teachers_coefficient(group, teachers_coeffs))

        # После выставления весов всем группам, ставим "наиболее ценные" в начало списка.
        course.groups.sort(key=lambda g: groups_weights[g.uuid_], reverse=True)


def get_time_coefficient(group: Group, grouped_times: Dict[int, List[LessonTimeChoice]]) -> float:
    res_coeff = 0

    for lesson in group.lessons:
        day = lesson.day

        if day not in grouped_times:
            res_coeff += 0.25
            continue

        tmp_coef = res_coeff

        for time in grouped_times[day]:
            if time.day == lesson.day and time.start <= lesson.start and lesson.end <= time.end:
                res_coeff += time_state_to_coefficient.get(time.state, MIN_COEFFICIENT)

        if res_coeff == tmp_coef:
            res_coeff += 0.25

    return res_coeff / len(group.lessons)


def get_teachers_coefficient(group: Group, preferred_coeffs: Dict[int, float]) -> float:
    res_coeff = 0

    for teacher in group.teachers:
        if teacher.id in preferred_coeffs:
            res_coeff += preferred_coeffs[teacher.id] * teacher_role_to_coefficient.get(teacher.role, MIN_COEFFICIENT)
        else:
            res_coeff += MIN_COEFFICIENT

    return res_coeff / len(group.teachers)


def get_preffered_teachers_coefficients(teachers: List[TeacherChoice]) -> Dict[int, float]:
    teacher_to_coeff = dict()
    step = (1 - 0.25) / (len(teachers) - 1)

    for teacher in teachers:
        teacher_to_coeff[teacher.uuid] = 1 - teacher.place * step

    return teacher_to_coeff


def get_times_grouped_by_day(selected_times: List[LessonTimeChoice]) -> Dict[int, List[LessonTimeChoice]]:
    all_times = dict()

    for time in selected_times:
        day = int(time.day)
        if day in all_times:
            all_times[day].append(time)
        else:
            all_times[day] = [time]

    return all_times
