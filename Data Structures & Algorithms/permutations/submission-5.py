class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # ALL PERMUTATIONS RAHHHHHHH

        # BACKTRACKING


        # for each starting position call backtrack
        res = []
        seen = set()
        # [1,2,3,3]
        def backtrack(curArr):
            nonlocal res
            if len(curArr) == len(nums):
                res.append(curArr.copy())
                return
            
            for i in range(0, len(nums)):
                if i not in seen:
                    seen.add(i)
                    curArr.append(nums[i])
                    backtrack(curArr)
                    # backtracking step
                    curArr.pop()
                    seen.remove(i)
        arr = []
        backtrack(arr)            
        return list(res)