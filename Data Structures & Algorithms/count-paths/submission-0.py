class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = 1
        arrows = m + n - 2

        for arrow in range(1, arrows+1):
            path *= arrow
        
        for i in range(1, m):
            path /= i
        
        for j in range(1, n):
            path /= j
        
        return int(path)

        