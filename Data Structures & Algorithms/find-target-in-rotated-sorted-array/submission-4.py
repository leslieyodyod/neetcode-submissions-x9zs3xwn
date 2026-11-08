class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if left is less than right
            #binary search like normal
        #else if left is greater than right 
            #compare m to left (determine rotation)
                #if m is greater than target
                    #move left to after m 
                #if m is less than target
                    #move right to before m 
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
                


                    
            

            

                    