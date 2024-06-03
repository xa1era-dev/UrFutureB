import unittest

from core import Competence, Tag, Profession, Course
from logics import sort_competences_by_intersection_with_profession_tags, get_courses_sorted_by_relevance
from logics.sorting import get_all_tags


class TestSorting(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = [Tag(id=1), Tag(id=2), Tag(id=3)]

    def test_competences_sorting(self):
        competences = [
            Competence(id=1, tags=[Tag(id=1)]),
            Competence(id=2, tags=[Tag(id=1), Tag(id=2), Tag(id=3)]),
            Competence(id=3, tags=[]),
            Competence(id=4, tags=[Tag(id=2), Tag(id=3)])
        ]

        sort_competences_by_intersection_with_profession_tags(Profession(tags=self.tags), competences)
        tags = get_all_tags(competences)
        self.assertSequenceEqual([comp.id for comp in competences], [2, 4, 1, 3])
        self.assertSequenceEqual(list(tags), [Tag(id=1), Tag(id=2), Tag(id=3)])

    def test_courses_sorting(self):
        course1 = Course(id=1, tags=[Tag(id=1), Tag(id=5), Tag(id=10), Tag(id=15), Tag(id=20)])
        course2 = Course(id=2, tags=[Tag(id=10), Tag(id=15)])
        course3 = Course(id=3, tags=[Tag(id=15), Tag(id=100), Tag(id=50), Tag(id=75)])
        course4 = Course(id=4, tags=[Tag(id=1000), Tag(id=555)])

        comps_list = [
            Competence(tags=[Tag(id=100), Tag(id=75), Tag(id=404)]),
            Competence(tags=[Tag(id=15), Tag(id=1), Tag(id=50), Tag(id=5)]),
            Competence(tags=[Tag(id=20), Tag(id=100), Tag(id=50), Tag(id=75)])
        ]

        courses = [course1, course2, course3, course4]
        result = get_courses_sorted_by_relevance(courses, comps_list, remove_zeros=True)
        result_ids = [crs.id for crs in result]

        self.assertSequenceEqual(result_ids, [3, 1, 2])
