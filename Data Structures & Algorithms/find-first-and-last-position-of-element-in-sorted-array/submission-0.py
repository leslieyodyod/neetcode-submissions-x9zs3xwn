class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[r] > target:
                r -= 1
            elif nums[l] < target:
                l += 1
            else:
                return [l, r]
        return [-1, -1]