class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        
        for key, value in hashMap.items():
            if value > len(nums) // 2:
                return key
        