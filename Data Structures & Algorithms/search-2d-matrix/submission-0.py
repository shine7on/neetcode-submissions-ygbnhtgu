class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        for r in range(ROW):
            if matrix[r][0] == target or matrix[r][COL-1] == target:
                return True
            elif matrix[r][0] < target and target < matrix[r][COL-1]:
                for c in range(1,COL-1):
                    if target == matrix[r][c]:
                        return True 
        
        return False