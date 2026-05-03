class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index in range(len(nums)):
            num = nums[index]
            if num in hm:
                return [hm[num], index]
            hm[target-num] = index