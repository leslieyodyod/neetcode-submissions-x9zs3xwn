class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # seen = set()
        # for num in nums:
        #     seen.add(num)
        ptr1, ptr2 = 0, 1
        while ptr1 < ptr2 and ptr2 < len(nums):
            if nums[ptr1] == nums[ptr2]:
                nums.remove(nums[ptr2])
            else:
                ptr1 += 1
                ptr2 += 1
        return len(nums)

            
        