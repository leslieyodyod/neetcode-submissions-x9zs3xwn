class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i, v in enumerate(nums):
            pair = target - v
            if pair in hashNum:
                return [hashNum[pair], i]
            hashNum[v] = i
        # for i in range(len(nums) - 1):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]