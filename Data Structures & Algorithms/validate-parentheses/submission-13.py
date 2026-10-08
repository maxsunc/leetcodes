class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # store the expected values
        map = {"(" : ")", "{": "}","[":"]"}

        for c in s:
            if c in map:
                stack.append(map[c])
            else:
                # pop from stack and see if its good
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0