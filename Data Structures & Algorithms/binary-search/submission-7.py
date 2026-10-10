class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # if it no exiwt return - 1

        l,r = 0, len(nums) - 1

        while r >= l:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1