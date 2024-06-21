from core.models import Competence

from logics.sorting import get_course_average_relevance
from logics.weighters.course_weighter import CourseWeighter


class RelevanceCourseWeighter(CourseWeighter):
    def __init__(self, competences: list[Competence]):
        self.competences = competences

    def get_courses_weights(self, courses):
        tags = [comp.tag for comp in self.competences]
        return {crs.id: get_course_average_relevance(crs, tags) for crs in courses}
