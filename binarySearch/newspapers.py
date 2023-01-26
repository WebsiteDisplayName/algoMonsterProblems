from typing import List


def feasible(newspapers_read_times, num_coworkers, limit):
    reqWorker = 0
    timeCounter = 0
    for newspaper in newspapers_read_times:
        if timeCounter + newspaper > limit:
            reqWorker += 1
            timeCounter = 0
        timeCounter += newspaper
    if timeCounter != 0:
        reqWorker += 1
    return reqWorker <= num_coworkers


def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    # comparing lowest possible time to complete and highest possible time, answer is inbetween using binary search
    bestTime = -1
    while low <= high:
        mid = (low+high)//2
        if feasible(newspapers_read_times, num_coworkers, mid):
            bestTime = mid
            high = mid-1
        else:
            low = mid+1
    return bestTime


if __name__ == '__main__':
    newspapers_read_times = [int(x) for x in input().split()]
    num_coworkers = int(input())
    res = newspapers_split(newspapers_read_times, num_coworkers)
    print(res)
