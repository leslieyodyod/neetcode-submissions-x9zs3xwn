class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hashNum:
                return [hashNum[pair], i]
            hashNum[nums[i]] = i
        # for i in range(len(nums) - 1):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]