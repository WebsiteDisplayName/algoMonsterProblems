def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    possVals = list(range(1, n+1))
    low, high = 0, len(possVals)-1
    firstOcc = 0
    while low <= high:
        mid = (low+high)//2
        # first occ for where square of val is less than n
        if possVals[mid]**2 <= n:
            firstOcc = possVals[mid]
            low = mid+1
        else:
            high = mid-1
    return firstOcc


if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
