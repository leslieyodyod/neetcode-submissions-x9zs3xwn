class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNum, res = {}, []

        for num in nums:
            hashNum[num] = 1 + hashNum.get(num, 0)
        
        hashNum = sorted(hashNum, key=hashNum.get)
        hashNum = hashNum[::-1]
        return hashNum[:k]
        