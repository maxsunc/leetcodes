class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hand[i] = value written on ith card 
        # each gorup is size groupSize
        # cards consecutively increase by 1
        # return True if its possible to rearrange htem like this

        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        # store the next element wanted in some sort of hash set
        # [2 : 2, ] hashset with: [nextExpectedVal : curGroupSize,]
        # if a val in our sorted array doesn't exist in the hashmap then add it with a curGorupSize of 1
        # no one is expecting it so add what its expected
        # if a curGroupSize == groupSize pop it off
        # at the end check that the dict is empty or not
        hand.sort()
        # sort the array
        # all cards must be used in the end so it doesn't matter the order we take as long as their 
        # increasing consecutively
        # 1. len(hand) must be diviisble by groupsize
        heap = []

        for num in hand:
            if not heap:
                entry = (num + 1, 1)
                heapq.heappush(heap, entry)
            else:
                # check if the top element matches
                if heap[0][0] == num: # expected value matches
                    # expected value found
                    entry = heapq.heappop(heap)
                    newEntry = (num + 1,entry[1] + 1) # newExpectedValue new size
                    if newEntry[1] < groupSize:
                        heapq.heappush(heap, newEntry)
                else:
                    # no entry exists for this so push onto the heap
                    entry = (num + 1, 1)
                    heapq.heappush(heap, entry)
                # print(heap)
                    

        # print(map)
        return len(heap) == 0



        
