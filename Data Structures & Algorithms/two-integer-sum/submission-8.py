class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}

        for i,num in enumerate(nums):
            map[num] = i
        
        for i, num in enumerate(nums):
            newTarget = target - num

            if newTarget in map and map[newTarget] != i:
                return [i,map[newTarget]]