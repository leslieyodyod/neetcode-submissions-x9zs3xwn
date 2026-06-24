class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = {}

        for i in range(len(nums1)):
            hash1[i] = nums1[i]

        res = []
        
        for index, char in hash1.items():
            mapping = nums2.index(char)
            res.append(mapping)
        return res
        