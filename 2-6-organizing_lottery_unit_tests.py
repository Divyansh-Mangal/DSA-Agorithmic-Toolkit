import unittest
from organizing_lottery import points_cover, points_cover_naive
from random import randint

class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),

        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        num = 1
        while num<100000:
            print(num)
            num += 1
            n = randint(0,10)
            m = randint(1,10)
            starts = []
            ends = []
            for i in range(n):
                point = randint(-10, 1000)
                starts.append(point)
                ends.append(point + randint(0,100))

            points = []
            for _ in range(m):
                points.append(randint(-15, 1005))


            myanswer = points_cover(starts, ends, points)
            naiveanswer = points_cover_naive(starts, ends, points)

            if myanswer != naiveanswer:
                print(len(myanswer), len(naiveanswer))
                print(starts)
                print(ends)
                print(points)
                print(list(zip(myanswer, naiveanswer)))
                self.assertEqual(points_cover(starts, ends, points), points_cover_naive(starts, ends, points))
                break


    def test_large(self):
        pass


if __name__ == '__main__':
    unittest.main()
