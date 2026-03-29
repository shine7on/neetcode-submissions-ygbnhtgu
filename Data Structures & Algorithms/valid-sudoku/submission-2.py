class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROW,COL = len(board), len(board[0])
    
        def checkCol(c):
            res = set()
            for i in range(ROW):
                if board[i][c] in res and board[i][c] != '.':
                    return False
                res.add(board[i][c])
            return True
        
        def checkRow(r):
            res = set()
            for j in range(COL):
                if board[r][j] in res and board[r][j] != '.':
                    return False
                res.add(board[r][j])
            return True
        
        def checkGrid(r,c):
            res = set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j] in res and board[i][j] != '.':
                        return False
                    res.add(board[i][j])
            return True

        for i in range(COL):
            if not checkCol(i) or not checkRow(i):
                return False
        
        for i in range(0,ROW,3):
            for j in range(0,COL,3):
                if not checkGrid(i,j):
                    return False
        
        return True
        

        
        