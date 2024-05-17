import unittest

from logics import get_sorted_competences_and_all_tags, get_courses_sorted_by_relevance
from logics.tests.models import *


class TestSorting(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = [Tag(id=1), Tag(id=2), Tag(id=3)]

    def test_competences_sorting(self):
        competences = [
            Competence(1, [Tag(id=1)]),
            Competence(2, [Tag(id=1), Tag(id=2), Tag(id=3)]),
            Competence(3, []),
            Competence(4, [Tag(id=2), Tag(id=3)])
        ]

        comps, tags = get_sorted_competences_and_all_tags(Profession(self.tags), competences)
        self.assertSequenceEqual([comp.id for comp in comps], [2, 4, 1, 3])
        self.assertSequenceEqual(list(tags), [Tag(id=1), Tag(id=2), Tag(id=3)])

    def test_courses_sorting(self):
        course1 = Course(1, [Tag(id=1), Tag(id=5), Tag(id=10), Tag(id=15), Tag(id=20)])
        course2 = Course(2, [Tag(id=10), Tag(id=15)])
        course3 = Course(3, [Tag(id=15), Tag(id=100), Tag(id=50), Tag(id=75)])

        tags_lists = [
            [Tag(id=100), Tag(id=75), Tag(id=404)],
            [Tag(id=15), Tag(id=1), Tag(id=50), Tag(id=5)],
            [Tag(id=20), Tag(id=100), Tag(id=50), Tag(id=75)]
        ]

        sorted_courses = get_courses_sorted_by_relevance([course1, course2, course3], tags_lists)
        self.assertSequenceEqual([crs.id for crs in sorted_courses], [3, 1, 2])
