class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMatrix = [[0] * len(matrix) for r in range(len(matrix[0]))]
        row, col = len(matrix), len(matrix[0])
        for r in range(row):
            for c in range(col):
                newMatrix[c][r] = matrix[r][c]
        return newMatrix