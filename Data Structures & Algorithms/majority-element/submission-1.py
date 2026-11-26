class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}

        for num in nums:
            occ[num] = occ.get(num, 0) + 1
        
        for key in occ:
            if occ[key] > len(nums) // 2:
                return key
        return 0