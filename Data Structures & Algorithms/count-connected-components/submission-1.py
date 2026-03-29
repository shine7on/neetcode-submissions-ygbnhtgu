class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n

        # union search
        def find(n1):
            res = n1

            while res != parent[res]: # whem tehy are not loop
                parent[res] = parent[parent[res]]
                res = parent[res] # go to loot
            return res
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]: # p2 will be parent
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1,n2)
        return res