from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freqMap, maxVal, res = defaultdict(), len(grid[0]) ** 2, [0, 0]
        values = set(i for i in range(1, maxVal + 1))

        for i in range(1, maxVal + 1):
            freqMap[i] = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                freqMap[grid[r][c]] += 1
        
        for num, count in freqMap.items():
            if count > 1:
                res[0] = num
            elif count == 0:
                res[1] = num
        
        return res
            


        


            