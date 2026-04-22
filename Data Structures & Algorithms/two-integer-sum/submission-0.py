class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index in range(len(nums)):
            if nums[index] in hm:
                return [hm[nums[index]], index]
            diff = target - nums[index]
            hm[diff] = index

