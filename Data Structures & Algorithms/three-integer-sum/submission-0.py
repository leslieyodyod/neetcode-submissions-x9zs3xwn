class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = []

        for l in range(len(nums)):
            for m in range(l + 1, len(nums)):
                for r in range(m + 1, len(nums)):
                    if (nums[l] + nums[m] + nums[r]) == 0 and sorted([nums[l], nums[m], nums[r]]) not in seen:
                        seen.append(sorted([nums[l], nums[m], nums[r]]))
        
        return seen

