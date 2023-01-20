from typing import List


def find_boundary(arr: List[bool]) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        currIdx = (low + high)//2
        if arr[currIdx] == True and (arr[currIdx-1] == False or currIdx-1 < 0):
            return currIdx
        elif arr[currIdx] == True:
            high = currIdx-1
        elif arr[currIdx] == False:
            low = currIdx + 1
    return -1


if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
