class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        perf = [n * n for n in range(2**16)]

        l, r = 0, len(perf) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if perf[mid] > num:
                r = mid - 1 
            elif perf[mid] < num:
                l = mid + 1
            else:
                return True
        return False

