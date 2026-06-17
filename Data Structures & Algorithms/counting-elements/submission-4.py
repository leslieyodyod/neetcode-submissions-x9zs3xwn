class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        hashMap = {}

        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        for num, total in hashMap.items():
            if (num + 1) in hashMap:
                count += hashMap[num]
        
        return count 

        