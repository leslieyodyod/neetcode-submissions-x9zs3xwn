class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #helper function
        def merge(arr, L, M, R):
            left, right = arr[L: M + 1], arr[M + 1: R + 1]
            #pointers for arr to sort it and subarrays to compare values
            i, j, k = L, 0, 0
            #iterate through both subarrays and compare values
            while j < len(left) and k < len(right):
                #if left is less than or equal to right value
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                #increment i regardless to keep moving through array
                i += 1
            #if there are remaining values in left or right
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
                
        #merge sort function 
        def mergeSort(arr, l, r):
            #keep splitting until you get each value by itself
            if l == r:
                return arr
            #compute middle point
            m = (l + r) // 2
            #call function on left half 
            mergeSort(arr, l, m)
            #call function on right half
            mergeSort(arr, m + 1, r)
            #call helper function to merge each sorted half
            merge(arr, l, m, r)
            return arr
            

        return mergeSort(nums, 0, len(nums) - 1)
            
