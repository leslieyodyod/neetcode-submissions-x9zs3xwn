class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i in range(len(nums)):
            if target - nums[i] in hashNum.values():
                return [nums.index(target - nums[i]), i]
            hashNum[i] = nums[i]
        # for i in range(len(nums) - 1):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]