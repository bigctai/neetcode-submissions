class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        for i in range(len(nums)-3, -1, -1):
            if i + 3 >= len(nums):
                nums[i] = nums[i] + nums[i+2]
            else:
                nums[i] = nums[i] + max(nums[i+2], nums[i+3])
        return max(nums[0], nums[1])