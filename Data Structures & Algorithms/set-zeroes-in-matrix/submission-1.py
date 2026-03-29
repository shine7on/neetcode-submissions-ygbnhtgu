class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])
        doneRow = set()
        doneCol = set()

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    doneRow.add(r)
                    doneCol.add(c)

        for r in range(ROW):
            if r in doneRow:
                for c in range(COL):
                    matrix[r][c] = 0
        
        for c in range(COL):
            if c in doneCol:
                for r in range(ROW):
                    matrix[r][c] = 0

        
        