class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # answer[i] is equal to the product of all elements of nums except nums[i]

        # use a prefix prod array =
        # [1,2,3,4]
        # [1,1,2,6]
        # [24,12,4,1]

        pre = [1 for i in range(0,len(nums))]
        suf = [1 for i in range(0,len(nums))]

        # build pre
        curProd = 1
        for i,n in enumerate(nums):
            pre[i] = curProd
            curProd *= n
        curProd = 1
        for i in range(len(nums) - 1, - 1, -1):
            suf[i] = curProd
            curProd *= nums[i]
        
        res = [1 for i in range(0,len(nums))]

        for i in range(0, len(nums)):
            res[i] = suf[i] * pre[i]
        return res
        # O(N) space O(N) time