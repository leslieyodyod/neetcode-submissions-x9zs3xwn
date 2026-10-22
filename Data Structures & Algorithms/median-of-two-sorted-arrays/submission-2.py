class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = sorted(nums1 + nums2)
        totalLen = len(total)
        medianIdx = (totalLen - 1) // 2
        if totalLen % 2 == 0:
            return sum(total[medianIdx: medianIdx + 2]) / 2
        else:
            return total[medianIdx]
