class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # given a nums array
        # find all pairs of 3 integers that sum up to 0
        nums.sort() # O(nlogn)
        res = []

        # O(N^2)
        for i,num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip duplicate values
            l,r = i + 1, len(nums) - 1
            target = -num
            # keep track of previously seen: only for one value is needed cuz its a sum
            prevIndex = -1
            while r > l:
                # print(f"{l},{r},{i}")
                curSum = nums[l] + nums[r]
                if curSum == target:
                    if prevIndex != -1 and nums[prevIndex] == nums[l]:
                        # move l to a new value
                        l+= 1
                        continue
                    # we found one
                    res.append([num,nums[l],nums[r]])
                    prevIndex = l
                elif curSum > target:
                    r -= 1
                else:
                    l += 1
        
        return res