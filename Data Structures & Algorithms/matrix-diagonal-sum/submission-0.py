class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        d1, d2 = 0, len(mat) - 1
        res = 0
        #calculate first diagonal
        for r in range(len(mat)):
            if d1!= d2:
                res += mat[r][d1]
                res += mat[r][d2]
            else:
                res += mat[r][d1]
            d1 += 1
            d2 -= 1
        return res
        