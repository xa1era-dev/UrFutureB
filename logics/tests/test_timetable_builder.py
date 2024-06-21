import unittest

from logics.timetable_builder import TimetableBuilder


class TestTimetableBuilder(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_full_timetable(self):
        builder = TimetableBuilder(week_length=7, lessons_at_day=10)

        for i in range(7):
            builder.add_lesson(day=i, start=0, end=9)

        inserted = False
        matrix = builder.get_time_matrix()

        for i in range(7):
            inserted |= builder.can_add_lesson(day=i, start=0, end=9)

        self.assertEqual(sum(matrix), 7 * 10)
        self.assertEqual(inserted, False)

    def test_lessons_intersections(self):
        builder = TimetableBuilder(week_length=7, lessons_at_day=10)
        builder.add_lesson(day=2, start=4, end=8)

        self.assertEqual(builder.can_add_lesson(day=2, start=4, end=8), False)
        self.assertEqual(builder.can_add_lesson(day=2, start=0, end=9), False)
        self.assertEqual(builder.can_add_lesson(day=2, start=0, end=6), False)
        self.assertEqual(builder.can_add_lesson(day=2, start=6, end=9), False)
        self.assertEqual(builder.can_add_lesson(day=2, start=4, end=4), False)
        self.assertEqual(builder.can_add_lesson(day=2, start=8, end=8), False)

    def test_lessons_without_intersections(self):
        builder = TimetableBuilder(week_length=7, lessons_at_day=10)
        builder.add_lesson(day=2, start=4, end=8)

        self.assertEqual(builder.can_add_lesson(day=1, start=4, end=8), True)
        self.assertEqual(builder.can_add_lesson(day=3, start=4, end=8), True)
        self.assertEqual(builder.can_add_lesson(day=2, start=0, end=1), True)
        self.assertEqual(builder.can_add_lesson(day=2, start=9, end=9), True)
