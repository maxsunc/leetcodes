class Solution:
    def simplifyPath(self, path: str) -> str:
        # change path into simplified path
        path += "/"
        # .. = prev directory
        # multiple / = /

        # ignore any other /'s when the top value is slash

        # . does nothing,
        # .. goes back, so we should pop off our stack

        # Use a stack
        # keep track of the current directroy:
        # its always valid
        curStr = ""
        stackRes = []
        # when we encounter /, evaluate curStr

        for i,c in enumerate(path):
            if c == "/":
                # evaluate curStr, if its non empty
                if len(curStr) != 0 and curStr != ".":
                    if curStr == "..":
                        if stackRes:
                            stackRes.pop()
                    else:
                        stackRes.append(curStr)
                curStr = ""
                # move until there are no more "/"
                lastSlashPos = i
                for j in range(i, len(path)):
                    if path[j] == "/":
                        lastSlashPos = j
                i = lastSlashPos # skips extra slashes
            else:
                # value we just append to the str
                curStr += c
        
        res = ""
        # print(stackRes)
        for c in stackRes:
            res += f"/{c}"
        return res if len(res) != 0 else "/"