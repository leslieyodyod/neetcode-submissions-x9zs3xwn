class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cutoff = len(nums) // 2
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for n, f in freq.items():
            if f >= cutoff:
                return n 