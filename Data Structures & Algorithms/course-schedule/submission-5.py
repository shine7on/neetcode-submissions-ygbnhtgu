class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # store in the hashmap
        hashmap = {i:[] for i in range(numCourses)}
        for i,j in prerequisites: 
            hashmap[i].append(j)
        
        visiting = set()
        
        def dfs(crs):
            if crs in visiting:
                return False
            if hashmap[crs] == []: # no prerequisite
                return True

            visiting.add(crs)
            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            hashmap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        