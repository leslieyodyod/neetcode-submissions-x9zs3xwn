class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i, num in enumerate(nums):
            complement = target - num
            if num in hashNum:
                return [hashNum[num], i]
            hashNum[complement] = i