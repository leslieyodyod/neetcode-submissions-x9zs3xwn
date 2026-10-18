class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in hashNum:
                return [hashNum[nums[i]], i]
            hashNum[diff] = i