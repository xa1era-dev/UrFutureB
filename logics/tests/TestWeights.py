import unittest

from core.models.models import Course, Lesson, Tag
from logics.weights import get_course_weight


class TestWeights(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.course = Course()
        self.tags = [Tag(id=1), Tag(id=2), Tag(id=3), Tag(id=4)]

    def test_no_intersection(self):
        self.course.lessons = [Lesson(id=0)]
        self.assertEqual(get_course_weight(self.course, self.tags), 0)

    def test_full_intersection(self):
        self.course.lessons = [Lesson(id=1), Lesson(id=2), Lesson(id=3), Lesson(id=4)]
        self.assertEqual(get_course_weight(self.course, self.tags), 1)

    def test_half_intersection(self):
        self.course.lessons = [Lesson(id=1), Lesson(id=2)]
        self.assertEqual(get_course_weight(self.course, self.tags), 0.5)
