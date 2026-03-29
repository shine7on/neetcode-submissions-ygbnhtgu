class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)


        for i in range(n+1):
            count = 0
            index = i
            print(f"now {index}")
            while(i>0):
                if i%2 == 1:
                    count+=1
                i = int(i/2)
                print(f"computing {i}")
            
            res[index] = count
        
        return res


        