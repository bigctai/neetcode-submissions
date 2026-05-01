class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            index = int((start + end + 1) / 2)
            if nums[index-1] > nums[index]:
                return nums[index]
            if nums[index] < nums[end]:
                end = index
            else:
                start = index
        if nums[0] > nums[len(nums)-1]:
            return nums[end]
        return nums[0]
