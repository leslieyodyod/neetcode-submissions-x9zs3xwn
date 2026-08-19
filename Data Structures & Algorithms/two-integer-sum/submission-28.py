class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        hashNum = {}

        for i in range(len(nums)):
            if target - nums[i] in hashNum:
                return [nums.index(target - nums[i]), i]
            hashNum[nums[i]] = target - nums[i]