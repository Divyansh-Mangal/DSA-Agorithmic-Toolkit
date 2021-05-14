# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

def update_segments(old_segments, last_visit):

    update_segments = []
    for segment in old_segments:
        if segment.start <= last_visit <= segment.end:
            pass
        else:
            update_segments.append(segment)

    return update_segments



def compute_optimal_points(segments):

    visits = []

    while len(segments) != 0:
        right_point = []
        for segment in segments:
            right_point.append(segment.end)

        visits.append(min(right_point))

        segments = update_segments(segments, visits[-1])

    visits = set(visits)
    visits = list(visits)
    return visits


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    #n, *data = map(int, input().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
