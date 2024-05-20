import unittest

from core import Course, Tag
from logics.weights import get_course_weight


class TestWeights(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course = Course(id=0, tags=[])
        self.tags = [Tag(id=1), Tag(id=2), Tag(id=3), Tag(id=4)]

    def test_no_intersection(self):
        self.course.tags = [Tag(id=0)]
        self.assertEqual(get_course_weight(self.course, self.tags), 0)

    def test_full_intersection(self):
        self.course.tags = [Tag(id=1), Tag(id=2), Tag(id=3), Tag(id=4)]
        self.assertEqual(get_course_weight(self.course, self.tags), 1)

    def test_half_intersection(self):
        self.course.tags = [Tag(id=1), Tag(id=2)]
        self.assertEqual(get_course_weight(self.course, self.tags), 0.5)

    def test_no_tags(self):
        self.assertEqual(get_course_weight(self.course, []), 0.0)
