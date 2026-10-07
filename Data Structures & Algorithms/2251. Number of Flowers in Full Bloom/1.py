class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        # is the flower array sorted by start always?

        # idea: sort the people array by the start times but keep track of their original index
        n = len(people)
        m = len(flowers)



        # use a minHeap to store the endtimes of the flowers
        # for every people we look throgh;


        # 1. check if the start position for the flower can be added
        # then add the endPosition to the heap

        # 2. check if any end positions have expired in the heap then pop off

        # 3. determine the answer at the original index
        # O(nlog(m) + m + nlogn)
        res = [0 for i in range(0, n)]

        peoplesSorted = []
        for i,p in enumerate(people):
            peoplesSorted.append((p,i))
        peoplesSorted.sort()
        flowers.sort()
        heap = []
        flowerIndex = 0

        for p in peoplesSorted:
            while m > flowerIndex and flowers[flowerIndex][0] <= p[0]:
                heapq.heappush(heap,flowers[flowerIndex][1])
                flowerIndex += 1
            
            # 2: 
            while heap and heap[0] < p[0]:
                heapq.heappop(heap)
            # number of flowers is simply len(heap)
            trueIndex = p[1]
            # print(f"looking at {heap} at {p[0]}")
            res[trueIndex] = len(heap)
        return res


