class Solution:
    def trap(self, height: list[int]) -> int:
        l,r = 0, len(height) - 1
        leftMax,rightMax = 0, 0
        # we only care about the min(leftMax,rightMax)
        # if leftMax >= rightMax:
        # calculate and add to result for right value since we know left is sufficently big enough
        # update rightMax
        # advance rigth pointer
        res = 0
        while r >= l:
            if leftMax >= rightMax:
                res += rightMax - height[r] if height[r] < rightMax else 0
                rightMax = max(rightMax,height[r])
                r -= 1
            else:
                res += leftMax - height[l] if height[l] < leftMax else 0
                leftMax = max(leftMax,height[l])
                l += 1
        return res

