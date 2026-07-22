class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # initialize return list
        # sort nums

        # four pointers
        # i is fixed
        # j is fixed
        # l and r coverge to target

        # checks to do
        # if i > 0 and nums[i] == nums[i - 1], break
        # if j - i > 1 and nums[j] == nums[j - 1], continue

        res = []
        nums.sort()

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    four_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if four_sum < target:
                        l += 1
                    elif four_sum > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r:
                            l += 1
                            if nums[l] != nums[l - 1]:
                                break
        
        return res

                    
                


        
        



