class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        min_i, min_j = float('inf'), float('inf')
        seen = set()
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    if i not in seen and j not in seen and i != j:
                        res.append(min(min_i, i))
                        res.append(min(min_j, j))
                        seen.add(i)
                        seen.add(j)
        return res
                    