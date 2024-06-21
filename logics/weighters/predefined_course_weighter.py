from logics.weighters.course_weighter import CourseWeighter


class PredefinedCourseWeighter(CourseWeighter):
    def __init__(self, courses_weights: dict[int, float]):
        self.courses_weights = courses_weights

    def get_courses_weights(self, courses):
        return {self.courses_weights[crs.id] for crs in courses}
