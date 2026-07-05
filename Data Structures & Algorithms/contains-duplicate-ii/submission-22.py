class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        seen = set()
        #create a sliding window of size k 
        #check if there are duplicates using a set
        #if yes return true 
        #if never return true, return false
        for r in range(len(nums)):
            if r - l > k:
                seen.remove(nums[l])
                l += 1
            if nums[r] in seen:
                return True 
            seen.add(nums[r])
        return False

            

