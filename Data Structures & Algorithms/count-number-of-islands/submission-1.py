class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        def dfs(i,j,grid):

            grid[i][j] = 'X'

            if i > 0:
                if grid[i-1][j] == "1":
                    grid[i-1][j] = 'X'
                    grid = dfs(i-1,j,grid)
            
            if i < len(grid) - 1:
                if grid[i+1][j] == "1":
                    grid[i+1][j] = 'X'
                    dfs(i+1,j,grid)

            if j > 0:
                if grid[i][j-1] == "1":
                    grid[i][j-1] = 'X'
                    dfs(i,j-1,grid)

            if j < len(grid[0]) - 1:
                if grid[i][j+1] == "1":
                    grid[i][j+1] = 'X'
                    dfs(i,j+1,grid)

            return grid
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print(f"here: {i}, {j}")
                    grid = dfs(i,j,grid)
                    count += 1 # found one iland
        return count
        