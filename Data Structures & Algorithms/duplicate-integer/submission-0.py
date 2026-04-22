class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        deduplicated_nums = {}
        for num in nums:
            if num in deduplicated_nums:
                return True
            else:
                deduplicated_nums[num] = True
        return False