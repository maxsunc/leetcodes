class Solution:
    def trap(self, height: list[int]) -> int:
        # keep track of the max values coming from both sides


        # preMax max seen up to this point
        # sufMax

        # itereate through heights:
        # if the height > preMax or sufMax dont add
        # else then calculate it with: min(preMax[i],sufMax[i]) 
        preMax,sufMax = [], []
        maxVal = 0
        for i in range(0, len(height)):
            preMax.append(maxVal)
            maxVal = max(maxVal, height[i])
        
        maxVal = 0
        for i in range(len(height)-1, -1, -1):
            sufMax.append(maxVal)
            maxVal = max(maxVal,height[i])
        sufMax.reverse()
        # print(preMax)
        # print(sufMax)
        res = 0
        for i,h in enumerate(height):
            # print(f"checking for {h} at {i} for {(sufMax[i],preMax[i])}")
            if h < min(sufMax[i],preMax[i]):
                # print(f"proc for {h} ")
                res += min(sufMax[i],preMax[i]) - h
        return res
                