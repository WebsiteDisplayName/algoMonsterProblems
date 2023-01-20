  from typing import List

   def binary_search(arr: List[int], target: int) -> int:
        # WRITE YOUR BRILLIANT CODE HERE
        # [0,1,2,3,4,5,6,7,8,9]
        # val 4 is at idx 5
        low = 0
        high = len(arr) - 1
        ticker = 0
        while low <= high:
            mid = (high+low)//2
            # print(f"low: {low}")
            # print(f"mid: {mid}")
            # print(f"high: {high}")
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid+1
            elif arr[mid] > target:
                high = mid-1

            ticker += 1
            if ticker > 20:
                break
        return -1

    # arr = [10,20], target = 20, ans = 1

    if __name__ == '__main__':
        arr = [int(x) for x in input().split()]
        target = int(input())
        res = binary_search(arr, target)
        print(res)
