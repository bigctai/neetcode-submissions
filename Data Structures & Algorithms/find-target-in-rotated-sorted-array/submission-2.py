class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            index = int((end + start) / 2)
            if nums[index] == target:
                return index
            if nums[end] == target:
                return end
            cycle = nums[end] < nums[index]
            if nums[index] > target and nums[end] > target and cycle:
                start = index + 1
            elif nums[index] < target and nums[end] > target:
                start = index + 1
            elif nums[index] < target and nums[end] < target and cycle:
                start = index + 1
            elif nums[index] > target and nums[end] < target:
                end = index - 1
            elif nums[index] > target and nums[end] > target and not cycle:
                end = index - 1
            else:
                end = index - 1
        if nums[index] == target:
            return index
        return -1
