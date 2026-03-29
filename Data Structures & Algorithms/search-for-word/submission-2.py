class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        X = len(board[0])
        Y = len(board)

        path = set()

        def dfs(x, y, i, path):
            
            if i == len(word):
                return True

            print(word[i])

            if x < 0 or x >= X or y < 0 or y >= Y or i > len(word):
                print("this")
                print(x,y,i)
                return False
            print(y)
            if word[i] != board[y][x]:
                return False
            if (x,y) in path:
                return False

            path.add((x,y))
            
            # letter matchs! -> next letter
            print("yey")
            i += 1
            neighbor = dfs(x-1, y, i, path) or dfs(x, y-1, i, path) or dfs(x, y+1, i, path) or dfs(x+1, y, i, path)

            path.remove((x,y))
            return neighbor

        print(X)
        
        for x in range(X):
            for y in range(Y):
                if board[y][x] == word[0]:
                    if dfs(x, y, 0, path):
                        return True
        
        return False
