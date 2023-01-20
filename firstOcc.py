from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    low, high = 0, len(arr)-1
    firstOcc = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= target:
            high = mid-1
            if arr[mid] == target:
                firstOcc = mid
        else:
            low = mid+1
    return firstOcc


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)
