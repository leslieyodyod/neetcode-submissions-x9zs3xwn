class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNum = {}
        res, maxN = [], None

        for num in nums:
            hashNum[num] = 1 + hashNum.get(num, 0)
        
        while k:
            maxN = max(hashNum, key=hashNum.get)
            res.append(maxN)
            del hashNum[maxN]
            k -= 1
        return res
            
            