class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights) # height: i
        col = len(heights[0]) # width: j

        dirP = ([1,0], [0,1], [-1,0], [0,-1]) 
        # dirA = ([-1,0], [0,-1]) 
        pacific = set()
        atlantic = set()
        prev = float('-inf')

        def dfs(i,j,dire,prev,setn):
            if i < 0 or i >= row or j < 0 or j >= col:
                print(f"imhere {i}, {j}")
                return

            if prev > heights[i][j]:
                print(f"break: {prev}, {heights[i][j]}")
                return            
            else:
                print(f"adding {i}, {j} in {prev}")
                if (i,j) in setn:
                    return
                else:
                    setn.add((i,j))
                    prev = heights[i][j]
                    if len(setn) >= row*col:
                        return
                    for dr, dc in dire:
                        dfs(i+dr, j+dc, dire, prev, setn)
            
        for j in range(col):
            dfs(0,j,dirP,prev,pacific)
            print("done with first pacific")
            dfs(row-1,j,dirP,prev,atlantic)
            print("done with first atl")
        
        for i in range(row):
            dfs(i,0,dirP,prev,pacific)
            print("done with 2nd pacific")
            dfs(i,col-1,dirP,prev,atlantic)
            print("done with 2nd atl")
        
        print(pacific, atlantic)
        
        return list(pacific.intersection(atlantic))


