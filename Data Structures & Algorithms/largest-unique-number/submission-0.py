class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        maxOnce = float('-inf')

        for num in freq:
            if freq[num] == 1:
                maxOnce = max(num, maxOnce)
        
        return maxOnce if 1 in freq.values() else -1
        