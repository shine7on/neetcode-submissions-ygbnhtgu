class Solution:
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] # put in the globl to store

        def dfs(i, cur, total):
            if total == target: # found result
                res.append(cur.copy()) # add the comb in result
                return
            if i >= len(nums) or total > target: # can not chose anymore
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0,[],0)
        return res
            

