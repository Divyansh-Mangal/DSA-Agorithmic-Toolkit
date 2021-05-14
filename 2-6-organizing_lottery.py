# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def binary_search(lst,key,high,low):
    import math
    index = 0

    if key < lst[0]:
        return -1
    elif key > lst[high]:
        return high

    mid = math.floor((high + low) / 2)

    if key == lst[mid]:
        return mid
    elif key > lst[mid]:
        low = mid + 1
        index = binary_search(lst, key, high, low)
    elif key < lst[mid]:
        high = mid - 1
        index = binary_search(lst, key, high, low)

    return index


def ordered_lines1(starts, ends):
    lines = dict(zip(starts, ends))

    starts.sort()
    ends.sort()

    return starts, ends, lines


def points_cover(starts, ends, points):
    if starts == []:
        return [0]*len(points)
    starts, ends, lines = ordered_lines1(starts, ends)
    #count_starts = Counter(ends)
    #count_ends = Counter(starts)

    winners = []
    for point in points:
        start_index = binary_search(starts, point, len(starts) - 1, 0)
        end_index = binary_search(ends, point, len(ends) - 1, 0)
        n = 0
        while True:
            if 0 < start_index + 1 < len(starts) and starts[start_index + 1] == starts[start_index]:
                start_index += 1
                n += 1
            else:
                break

        if point in ends:

            while True:
                if 0 <= (end_index - 1) < len(ends) and ends[end_index - 1] == ends[end_index]:
                    end_index -= 1
                else:
                    end_index -= 1
                    break

        winners.append(start_index - end_index)

    return winners





if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    #data = list(map(int, input().split()))

    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    #print(n,m, input_starts, input_ends)

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
