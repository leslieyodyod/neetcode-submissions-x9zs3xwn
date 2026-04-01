class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_count, max_count = 0, 0

        for num in nums:
            if num == 1:
                one_count += 1
                max_count = max(max_count, one_count)
            else:
                one_count = 0
        return max_count
            