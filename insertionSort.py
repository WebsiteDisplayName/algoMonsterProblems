from typing import List
from collections import deque


def sort_list(unsorted_list: List[int]) -> List[int]:
    for idx, num in enumerate(unsorted_list):
        current = idx
        while current > 0 and unsorted_list[current] < unsorted_list[current-1]:
            unsorted_list[current], unsorted_list[current -
                                                  1] = unsorted_list[current-1], unsorted_list[current]
            current -= 1
    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
