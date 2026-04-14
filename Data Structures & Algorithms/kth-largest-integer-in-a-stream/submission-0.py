class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort(reverse=True)

        count = 0
        for i in range(0,len(self.stream)):
            count += 1
            
            if count == self.k:
                return self.stream[i]
