class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            matrixMid = matrix[mid]
            if target not in matrixMid:
                if target > matrixMid[0]:
                    l = mid + 1
                elif target < matrixMid[0]:
                    r = mid - 1
            else:
                return True
        return False 
        
        