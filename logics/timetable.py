from collections import defaultdict

from logics import RelevanceCourseWeighter
from models.group import Group
from models.discipline import Discipline

from core.models import Competence, LessonTimeChoice, TeacherChoice, Course

from logics.timetable_builder import TimetableBuilder
from logics.constants import *


def build_timetable(
        compteneces: list[Competence],
        disciplines: list[Discipline],
        preferred_times: list[LessonTimeChoice],
        preferred_teachers: dict[int, list[TeacherChoice]],
        preferred_courses: dict[int, list[Course]],
        components_coeffs: ComponentsCoefficients) -> list[Group]:
    all_groups, group_coeffs = [], {}

    grouped_times = get_times_grouped_by_day(preferred_times)
    weighter = RelevanceCourseWeighter(compteneces)

    for discipline in disciplines:
        course_weights = weighter.get_courses_weights(discipline.courses)
        teachers = get_preffered_teachers_coefficients(preferred_teachers.get(discipline.id, []))

        for course in discipline.courses:
            for group in course.groups:
                time_mult = components_coeffs["time_coefficient"] * get_time_coefficient(group, grouped_times)
                teacher_mult = components_coeffs["teacher_coefficient"] * get_teachers_coefficient(group, teachers)

                course_mult = 1
                if not any(crs.id == course.id for crs in preferred_courses.get(discipline.id, [])):
                    course_mult = components_coeffs["course_coefficient"] * course_weights[course.id]

                group_coeffs[group.id] = time_mult * teacher_mult * course_mult
                all_groups.append(group)

    all_groups.sort(key=lambda grp: group_coeffs[grp.id], reverse=True)

    counter, max_counter, marked_courses = 0, len(disciplines), {}
    timetable_builder = TimetableBuilder(week_length=7, lessons_at_day=10)

    final_groups = []

    for group in all_groups:
        if counter == max_counter:
            break

        if marked_courses[group.course.id]:
            continue

        time_fit = True

        for lesson in group.lessons:
            time_fit &= timetable_builder.can_add_lesson(lesson.day, lesson.start, lesson.end)

            if time_fit is False:
                break

        if time_fit:
            for lesson in group.lessons:
                timetable_builder.add_lesson(lesson.day, lesson.start, lesson.end)

            marked_courses[group.course.id] = True
            final_groups.append(group)

            counter += 1

    if counter != max_counter:
        raise Exception("Something went wrong during timetable creation.")

    return final_groups


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
