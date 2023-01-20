from typing import List


# 3,4,5,1,2
# FFFTT
def find_min_rotated(arr: List[int]) -> int:
    low, high = 0, len(arr)-1
    minOcc = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] <= arr[high]:
            high = mid-1
            minOcc = mid
        else:
            low = mid+1

    return minOcc


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
