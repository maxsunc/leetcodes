class MedianFinder:

    def __init__(self):
        # never remoe any elements
        # brute force: keep track of a sorted array, just insert it in. addNum then becomes O(N) findmedian is O(1)
        # okay but not fast aenough

        # using two heaps

        # [1,2,3]
        # maxHeap (1st half of the array)
        # minHeap (2nd half of the array)
        # when doing add num. append to the least length value
        # every element in the maxHeap must be smaller than every element in the minHeap
        self.maxHeapFirst = []
        self.minHeapSecond = []
        self.size = 0

    def addNum(self, num: int) -> None:
        
        if (self.size % 2 == 0):
            # even length:
            heapq.heappush(self.maxHeapFirst, -num)
        else:
            # push to the less length
            if len(self.maxHeapFirst) > len(self.minHeapSecond):
                heapq.heappush(self.minHeapSecond, num)
            else:
                heapq.heappush(self.maxHeapFirst, -num)
        self.size += 1
        # rebalancing [100, 1], [2]
        if self.size >= 2 and -self.maxHeapFirst[0] > self.minHeapSecond[0]:
            val1 = -heapq.heappop(self.maxHeapFirst)
            val2 = heapq.heappop(self.minHeapSecond)
            heapq.heappush(self.maxHeapFirst, -val2)
            heapq.heappush(self.minHeapSecond,val1)


        
        

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (-self.maxHeapFirst[0] + self.minHeapSecond[0]) / 2
        
        return -self.maxHeapFirst[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()