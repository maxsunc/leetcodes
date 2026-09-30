class ListNode:
    def __init__(self, val, front=None, back=None):
        self.val = val
        self.front = front
        self.back = back


class LRUCache:

    def __init__(self, capacity: int):
        # all O(1) operations: 
        # initialize the LRU cache with size capacity:
        # key vlaue pairs with a specific size
        # storing the data: Use a simple dictionary: O(1) lookup time
        # keeping track of least recently used
        self.dict = {} # int : int
        self.keyToNode = {} # map the integer to node
        self.top = None
        self.back = None
        self.capacity = capacity


    def updateLRU(self, key):
        # assume it exists in keyToNode
        if self.top and self.top.val == key:
            return # no need to mess up the pointers
        # add it as normal, its the top
        node = self.keyToNode[key]
        if node == self.back:
            self.back = node.front
        # put this guy at the front
        prevTop = self.top
        # (1) <--> (2) <--> (3)
        if node.front:
            node.front.back = node.back
        if node.back:
            node.back.front = node.front
        node.front = None
        node.back = prevTop
        if prevTop:
            prevTop.front = node
        self.top = node

        if self.back == None:
            self.back = node




    def get(self, key: int) -> int:
        # return the vlaue of the key if it exists, otherwise -1
        # O(1)
        if key not in self.dict:
            return -1
        self.updateLRU(key)
        
        return self.dict[key]

        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
                self.dict[key] = value
                self.updateLRU(key)
                return
        # update the key if it exists
        # otherwise add a key value pair to the cache
        # if the numebr of keys exceed currently: evict the least recently used
        if len(self.dict) < self.capacity:
            # adding on a node
            self.dict[key] = value
            self.keyToNode[key] = ListNode(key)
            self.updateLRU(key)
        else:
            # case we're at capacity: the thing we're putting in is new
            # evict the least recently used
            # evict the back most dude
            valToPop = self.back.val
            node = self.back
            # get rid of pointers pointing to it
            if node.front:
                node.front.back = node.back
            # set a new back
            self.back = node.front

            self.dict.pop(valToPop)
            self.keyToNode.pop(valToPop)

            # add the vlaue now that we have space
            self.dict[key] = value
            self.keyToNode[key] = ListNode(key)
            self.updateLRU(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)