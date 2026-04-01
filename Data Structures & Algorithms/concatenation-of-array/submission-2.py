class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        stack = []

        ptr = 0

        while len(stack) < 2 * len(nums):
            if ptr == len(nums):
                ptr = 0
            else:
                stack.append(nums[ptr])
                ptr += 1
        
        return stack
