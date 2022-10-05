"""
We're given an array of interval pairs as input where each interval has a start and end timestamp.
The input array is sorted by starting timestamps.
Merge the overlapping intervals and return a new output array.
"""

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return 'Pair({0},{1})'.format(self.first, self.second)

def merge_intervals(v):
    print('input: {0}'.format(v))
    result = []

    temp = None
    for p in v:
        if temp is None:
            print(' setting temp to {0}'.format(p))
            temp = p
            continue

        print(' merging {0} with {1}'.format(temp, p))
        if temp.second >= p.first:
            if temp.second < p.second:
                temp.second = p.second
        else:
            print(' appending {0}'.format(temp))
            result.append(temp)
            print(' setting temp to {0}'.format(p))
            temp = p

    if temp is not None:
        print(' appending the last processed tuple: {0}'.format(temp))
        result.append(temp)

    print(' result: {0}'.format(result))
    return result

if __name__ == '__main__':
    merge_intervals([Pair(1, 5), Pair(3, 7), Pair(4, 6)])
    merge_intervals([1, 5] [3, 7] [4, 6])
    merge_intervals([1, 5] [4, 6] [6, 8] [11, 15])
    merge_intervals([3, 7] [6, 8] [10, 12] [11, 15])
    merge_intervals([1, 5])
    merge_intervals([1, 4] [4, 5])
