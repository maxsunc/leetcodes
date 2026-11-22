class TimeMap:

    def __init__(self):
        # store multiple values at different time stamps
        # retrieve keys value based on certain timestamp
        self.map = defaultdict(list) # key : {timestamp : value}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # binary search on timestamp
        arr = self.map[key]
        if len(arr) == 0:
            return ""

        # search for the highest entry iwth Time <= timestamp
        l,r = 0, len(arr) - 1
        resIndex = 0
        while r >= l:
            mid = l + (r-l) // 2
            if arr[mid][0] <= timestamp:
                resIndex = max(resIndex, mid)
                l = mid + 1
            else:
                r = mid - 1
        return arr[resIndex][1] if arr[resIndex][0] <= timestamp else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)