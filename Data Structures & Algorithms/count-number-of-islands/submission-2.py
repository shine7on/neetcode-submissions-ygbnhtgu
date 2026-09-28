class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        counter = 0

        # DFS
        def dfs(r,c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                if r != 0:
                    dfs(r-1, c) # up
                if c != 0:
                    dfs(r, c-1) # left
                if c < COL - 1:
                    dfs(r, c+1) # right
                if r < ROW - 1:
                    dfs(r+1, c) # down
            else:
                return

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    dfs(r,c)
                    counter += 1
        
        print(grid)
        return counter
