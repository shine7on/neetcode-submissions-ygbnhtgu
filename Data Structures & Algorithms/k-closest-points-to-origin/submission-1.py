class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (3,3) = √18 = 4.1.., (5,-1) = √26 = 5.09.., (-2,4) = √20 = 4.24...
        dists = [-10000000]*k
        heapq.heapify(dists)
        res = defaultdict(list)

        for x,y in points:
            print(x,y)
            dist = -math.sqrt(x**2 + y**2)
            print(dist, dists[0])
            if dists[0] == -10000000 or dist > dists[0]:
                print(dist)
                heapq.heappop(dists)
                heapq.heappush(dists, dist)
                res[dist].append([x,y])

        print(res, dists)
        output = []

        for d in dists:
            print(res[d])
            output.append(res[d][0])
            leng = len(res[d])
            temp = []
            for i in range(1,leng):
                temp.append(res[d][i])
            res[d] = temp

        return output