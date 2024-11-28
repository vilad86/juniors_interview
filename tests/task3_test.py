








import unittest

from task3.solution import (appearance,
                            get_intervals,
                            merge_intervals,
                            find_intersections)

class GetIntervalsFunction_Test(unittest.TestCase):
    #: Одного хватит, нам гарантировали всегда четное кол-во в списке.
    def test_get_intervals(self):
        intervals = [100, 200, 250, 251]
        expected = [(100, 200), (250, 251)]
        self.assertEqual(get_intervals(intervals), expected)

class MergeIntervalsFunction_Test(unittest.TestCase):
    def test_merge_intervals_case_1(self):
        intervals = [(100, 200), (250, 251)]
        expected = [(100, 200), (250, 251)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_merge_intervals_case_2(self):
        intervals = [(100, 200), (200, 251)]
        expected = [(100, 251)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_merge_intervals_case_3(self):
        intervals = [(100, 200), (201, 251)]
        expected = [(100, 200), (201, 251)]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_merge_intervals_case_4(self):
        intervals = [(100, 201), (200, 251)]
        expected = [(100, 251)]
        self.assertEqual(merge_intervals(intervals), expected)
        
class FindIntersectionsFunction_Test(unittest.TestCase):
    def test_find_intersections_case_1(self):
        interval_1 = [(100, 150), (200, 250)]
        interval_2 = [(100, 150), (200, 250)]
        expected = [(100, 150), (200, 250)]

        self.assertEqual(find_intersections(interval_1, interval_2), expected)
    
    def test_find_intersections_case_2(self):
        interval_1 = [(100, 150), (200, 250)]
        interval_2 = [(50, 100), (150, 200)]
        expected = []

        self.assertEqual(find_intersections(interval_1, interval_2), expected)

    def test_find_intersections_case_3(self):
        interval_1 = [(100, 150), (200, 250)]
        interval_2 = [(110, 160), (210, 240)]
        expected = [(110, 150), (210, 240)]

        self.assertEqual(find_intersections(interval_1, interval_2), expected)

class AppearanceFunction_Test(unittest.TestCase):
    def test_case_1(self):
        intervals = {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        }
        expected = 3117
        self.assertEqual(appearance(intervals), expected)

    def test_case_2(self):
        intervals = {
            'lesson': [1594702800, 1594706400],
            'pupil': [
                1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513,
                1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009,
                1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773,
                1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                1594706524, 1594706524, 1594706579, 1594706641
            ],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        }
        expected = 3577
        self.assertEqual(appearance(intervals), expected)

    def test_case_3(self):
        intervals = {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        }
        expected = 3565
        self.assertEqual(appearance(intervals), expected)

    def test_no_overlap(self):
        intervals = {
            'lesson': [2000, 5600],
            'pupil': [6000, 7000],
            'tutor': [8000, 9000]
        }
        expected = 0
        self.assertEqual(appearance(intervals), expected)

    def test_full_overlap(self):
        intervals = {
            'lesson': [2000, 5600],
            'pupil': [2000, 5600],
            'tutor': [2000, 5600]
        }
        expected = 3600
        self.assertEqual(appearance(intervals), expected)

    def test_partial_overlap(self):
        intervals = {
            'lesson': [2000, 5600],
            'pupil': [3000, 4000],
            'tutor': [3500, 4500]
        }
        expected = 500
        self.assertEqual(appearance(intervals), expected)
