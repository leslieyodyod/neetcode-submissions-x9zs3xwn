class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minVal = 1

        while minVal in nums:
            minVal += 1
        return minVal



            