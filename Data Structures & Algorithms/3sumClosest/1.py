class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # closest 3 integers to target
        
        # sort the array

        bestSum = sum(nums[0:3])

        nums.sort()

        for i,val in enumerate(nums):

            l = i + 1
            r = len(nums) - 1
            # [-1,2,1,-4]
            while r > l:
                curSum = nums[i] + nums[l] + nums[r]
                bestDiff = abs(target - bestSum)
                curDiff = abs(target - curSum)

                if bestDiff > curDiff:
                    bestSum = curSum
                    # res = [nums[i],nums[l],nums[r]]
                
                if curSum >= target:
                    r -= 1
                elif curSum < target:
                    l += 1
        

        return bestSum