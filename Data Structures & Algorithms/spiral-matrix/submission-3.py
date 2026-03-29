class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        COLUMN = len(matrix[0])
        ROW = len(matrix)
        cells = COLUMN * ROW
        i = 0
        res = []
        
        while cells > 0:
            column = COLUMN - i
            row = ROW - i
            if(row <= i or column <= i):
                break
            for c in range(i,column): # to right
                print(f'Right: {i}, {c}: {cells}')
                res.append(matrix[i][c])
                cells -= 1
            if (cells == 0): break
            for r in range(i+1,row): # to down
                print(f'Down: {r}, {column-1}')
                res.append(matrix[r][column-1])
                cells -= 1
            if (cells == 0): break
            for c in range(column-2,i-1,-1): # to left
                if (cells == 0): break
                print(f'Left: {row-1}, {c}: i-1 = {i-1}')
                res.append(matrix[row-1][c])
                cells -= 1
            for r in range(row-2,i,-1): # to up
                if (cells == 0): break
                print(f'Up: {r}, {c}')
                res.append(matrix[r][c])
                cells -= 1
            i += 1
        
        return res