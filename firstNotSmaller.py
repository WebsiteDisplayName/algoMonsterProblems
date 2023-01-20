from typing import List


def first_not_smaller(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    low = 0
    high = len(arr)-1
    firstOcc = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= target:
            firstOcc = mid
            high = mid-1
        else:
            low = mid+1
    return firstOcc


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)
