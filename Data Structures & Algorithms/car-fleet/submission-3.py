class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet, allCars = 0, len(position)
        res = []

        for i in range(allCars):
            res.append([position[i],speed[i]])

        res.sort()
        res.reverse()
        print(res)
        for i in range(1,allCars):
            j = i - 1
            # fleeting
            
            if (target - res[i][0]) / (res[i][1]) <= (target - res[j][0]) / (res[j][1]):
                allCars -= 1
                res[i][0] = res[j][0]
                res[i][1] = res[j][1]
                print(allCars)
            
        return allCars



        