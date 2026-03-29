class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for i in range(len(strs)):
            s = str(sorted(strs[i]))
            if hashmap.get(s) != None:
                (hashmap.get(s)).append(strs[i])
            else:
                hashmap[s] = [strs[i]]
        
        return list(hashmap.values())