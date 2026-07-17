class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashNum:
                return [hashNum[diff], i]
            hashNum[n] = i


            
        

        
            


        
            
        