class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 1st binary search to find the offset (lowest value)

        # find the min Index
        # if we find a valeu that is less than the minValue (final index)


        l,r = 0, len(nums) - 1
        minIndex = r

        while r >= l:
            mid = l + (r - l) // 2
            if nums[minIndex] >= nums[mid]:
                minIndex = mid
                r = mid - 1
            else:
                l = mid + 1

        # print(minIndex)

        n = len(nums)

        l,r = 0, len(nums) - 1

        while r >= l:
            mid = l + (r-l) // 2
            transformedMid = (mid + minIndex) % n
            if target == nums[transformedMid]:
                return transformedMid
            elif target > nums[transformedMid]:
                l = mid + 1
            else:
                 r = mid - 1
        return -1