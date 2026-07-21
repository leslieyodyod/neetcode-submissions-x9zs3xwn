class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}
        seen = set()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashNum:
                return [nums.index(diff), i]
            else:
                hashNum[nums[i]] = diff