class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # find he k closest points to origin

        # use a heap to store them:
        # min heap sorted by distance
        heap = []

        for point in points:
            dist = math.sqrt(math.pow(point[0],2) + math.pow(point[1],2))
            entry = (dist, point)
            heapq.heappush(heap,entry)
        res = []
        for i in range(0, k):
            if heap:
                entry = heapq.heappop(heap)
                res.append(entry[1])
        return res
            


