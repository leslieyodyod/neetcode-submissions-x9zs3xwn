class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return True
            #check if mid is equal to target
            #if not
                #if nums[l] is greater than nums[r]
                    #it's rotated 
                    #compare nums[l] with mid
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[r] < target <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        return False
                        #if it's greater
                            #if nums[l] is less than target
                                #r = mid - 1
                            #else:
                                #l = mid + 1
                        #if it's less than mid:
                            #if nums[l] is less than target:
                                #r = mid - 1
                            #if nums[l] greater than target:
                                #l = mid + 1
                    #return -1 if never found  
                        



        return False

