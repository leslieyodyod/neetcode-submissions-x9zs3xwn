class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, res = 0, 0

        for num in nums:
            if num != 1:
                count = 0
            else:
                count += 1
                res = max(count, res)
        return res 
                    
                    