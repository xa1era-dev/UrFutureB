from logics.weighters.course_weighter import CourseWeighter


class SteppingCourseWeighter(CourseWeighter):
    def __init__(self, min_value: float, max_value: float, step: float = 0.0):
        self.min_value = min_value
        self.max_value = max_value
        self.step = step

    def get_courses_weights(self, courses):
        weights = dict()
        step = self.step

        if self.step == 0.0:
            step = (self.max_value - self.min_value) / (len(courses) - 1)

        for i in range(len(courses)):
            weights[courses[i].id] = self.max_value - i * step

        return weights
