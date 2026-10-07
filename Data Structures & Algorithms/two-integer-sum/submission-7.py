class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # simple: Find indexes of two unique values that add up to target?
        # clarifying questions: Can there be negative values
        # is the input always guarunteed to be valid?

        # brute force: check all cases: Foreach num find another num if they add up to target
        # return them: O(N^2), O(1) space

        # sort the array first nlogn
        # use two pointers from the end and the start: move teh last pointer down
        # if the sum is greater and the first pointer up if the sum is less


        # O(N) space and time
        # keep a set, and as we iterate through check if it exists within the set

        # keep the set adding during runtime: Running set
        # [3,4,5,6]
        # Set: 3,4,5,6]

        # two pass: keep track of the value : Index
        # 2nd pass: iterate through and see if target - nums[i] is in the set
        
        # running set
        # since we would add to the running set after checking whether target - nums[i] exists
        # we wont run into getting the same index

        runningMap = {}
        for i, num in enumerate(nums):
            if (target - num) in runningMap:
                return [runningMap[target-num], i]
            runningMap[num] = i
        return [0,0]

