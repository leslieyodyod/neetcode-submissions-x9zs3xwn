class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        for key, value in d.items():
            if value > len(nums) // 3:
                res.append(key)

        return res