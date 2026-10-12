class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # find the max sum subarray
        # kadane's algorithm:

        # if the curSum ends up being negative 
        curSum = 0
        res = nums[0]
        for num in nums:
            if curSum < 0:
                # reset it, negative doesn't help us at all
                curSum = 0
            curSum += num
            res = max(res, curSum)
        return res
            