from typing import List


def peak_of_mountain_array(arr: List[int]) -> int:
    low, high = 0, len(arr)-1
    idxHold = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > arr[mid+1]:
            high = mid-1
            idxHold = mid
        else:
            low = mid+1
    return idxHold


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)
