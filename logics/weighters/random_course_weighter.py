from random import uniform
from logics.weighters.course_weighter import CourseWeighter


class RandomCourseWeighter(CourseWeighter):
    def __init__(self, min_weight: float, max_weight: float):
        self.min_weight = min_weight
        self.max_weight = max_weight

    def get_courses_weights(self, courses):
        return {crs.id: uniform(self.min_weight, self.max_weight) for crs in courses}
