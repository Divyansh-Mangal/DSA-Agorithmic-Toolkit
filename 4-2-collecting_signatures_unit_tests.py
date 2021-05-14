import unittest
from collecting_signatures import compute_optimal_points, Segment


class CollectingSignatures(unittest.TestCase):
    def test(self):
        for (segments, answer) in [
            ([Segment(1, 3), Segment(2, 5), Segment(3, 6)], 1),
            ([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)], 2),
            ([Segment(2, 6), Segment(2, 18), Segment(start=4, end=10), Segment(start=5, end=10), Segment(start=5, end=7), Segment(start=8, end=11), Segment(start=8, end=17), Segment(start=9, end=13), Segment(start=9, end=21), Segment(start=13, end=15), Segment(start=17, end=20), Segment(start=21, end=23)], 5)
        ]:
            self.assertEqual(len(compute_optimal_points(segments)), answer)


if __name__ == '__main__':
    unittest.main()
