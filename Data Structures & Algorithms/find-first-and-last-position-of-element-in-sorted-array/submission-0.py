class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # two binary searches
        # find the first and find the last
        firstPos = -1
        l,r = 0, len(nums) - 1

        while r >= l:
            mid = l + (r - l) // 2
            # [5,7,7,8,8,10]
            if target == nums[mid]:
                firstPos = mid
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        # print(firstPos)

        lastPos = -1
        l,r = 0, len(nums) - 1

        while r >= l:
            mid = l + (r - l) // 2
            # [5,7,7,8,8,10]
            if target == nums[mid]:
                lastPos = mid
                l = mid + 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return [firstPos, lastPos]