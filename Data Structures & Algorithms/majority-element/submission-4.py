class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashNum = {}

        for num in nums:
            hashNum[num] = 1 + hashNum.get(num, 0)
        
        for num in hashNum:
            if hashNum[num] > (len(nums) // 2):
                return num