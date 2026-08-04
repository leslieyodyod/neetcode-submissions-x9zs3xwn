class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}

        if len(nums) < 2:
            return nums[0]

        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
                if hashMap.get(nums[i]) > len(nums) // 2:
                    return nums[i]
            else:
                hashMap[nums[i]] = 1
        
        
        