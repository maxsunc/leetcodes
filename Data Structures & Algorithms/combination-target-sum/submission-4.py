class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # find a lsit of all unique combinations of candidates where the numbers sum up to target

        # backtracking problem, try all cases
        res = []
        def backtrack(arr,i,curSum):
            nonlocal res
            if curSum == target:
                res.append(arr.copy())
                return
            elif curSum > target or i >= len(candidates):
                return
            
            # take value at i, stay here
            arr.append(candidates[i])
            curSum += candidates[i]
            backtrack(arr, i, curSum)
            arr.pop()
            curSum -= candidates[i]

            backtrack(arr, i + 1, curSum)
        backtrack([], 0, 0)
        return res
