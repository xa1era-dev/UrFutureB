from collections import defaultdict

# TODO: Перейти на использование моделей, вместо схем.
from schemas.group import Group
from schemas.discipline import Discipline

from core.models import Competence, LessonTimeChoice, TeacherChoice, Course

from logics.weighters.course_weighter import CourseWeighter
from logics.timetable_builder import TimetableBuilder
from logics.constants import *


def build_timetable(
        compteneces: list[Competence],
        disciplines: list[Discipline],
        preferred_times: list[LessonTimeChoice],
        preferred_teachers: dict[int, list[TeacherChoice]],
        preferred_courses: dict[int, list[Course]],
        course_weighter: CourseWeighter,
        components_coeffs: ComponentsCoefficients) -> list[Group]:
    """
    Полное описание работы алгоритма.
    """
    pass


def try_choose_group(courses: list[Course], timetable_builder: TimetableBuilder) -> tuple[Course, Group] | None:
    for course in courses:
        for group in course.groups:
            time_fit = True

            for lesson in group.lessons:
                time_fit &= timetable_builder.can_add_lesson(lesson.day, lesson.start, lesson.end)

            if time_fit:
                for lesson in group.lessons:
                    timetable_builder.add_lesson(lesson.day, lesson.start, lesson.end)

                return course, group

    return None


def sort_courses_groups(
        courses: list[Course],
        grouped_times: dict[int, list[LessonTimeChoice]],
        teachers_coeffs: dict[int, float]) -> None:
    for course in courses:
        groups_weights = dict()

        for group in course.groups:
            groups_weights[group.uuid_] = \
                (get_time_coefficient(group, grouped_times) * get_teachers_coefficient(group, teachers_coeffs))

        course.groups.sort(key=lambda g: groups_weights[g.uuid_], reverse=True)


def get_time_coefficient(group: Group, grouped_times: dict[int, list[LessonTimeChoice]]) -> float:
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


def get_teachers_coefficient(group: Group, preferred_coeffs: dict[int, float]) -> float:
    res_coeff = 0

    for teacher in group.teachers:
        if teacher.id in preferred_coeffs:
            res_coeff += preferred_coeffs[teacher.id] * teacher_role_to_coefficient.get(teacher.role, MIN_COEFFICIENT)
        else:
            res_coeff += MIN_COEFFICIENT

    return res_coeff / len(group.teachers)


def get_preffered_teachers_coefficients(teachers: list[TeacherChoice]) -> dict[int, float]:
    teacher_to_coeff = dict()
    step = (1 - 0.25) / (len(teachers) - 1)

    for teacher in teachers:
        teacher_to_coeff[teacher.uuid] = 1 - teacher.place * step

    return teacher_to_coeff


def get_times_grouped_by_day(times: list[LessonTimeChoice]) -> dict[int, list[LessonTimeChoice]]:
    all_times = defaultdict(list)

    for time in times:
        all_times[time.day].append(time)

    return all_times
