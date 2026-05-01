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
        return nums[0]
