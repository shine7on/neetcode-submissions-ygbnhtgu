class MedianFinder:

    def __init__(self):
        self.li = []

    def addNum(self, num: int) -> None:
        self.li.append(num)

    def findMedian(self) -> float:
        self.li.sort()
        length = len(self.li)
        mid = length//2
        if length % 2 == 1:
            return self.li[mid]
        
        return (self.li[mid-1]+self.li[mid])/2
        
        