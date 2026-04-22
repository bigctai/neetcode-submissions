class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = set(nums)
        longest = 0
        for num in list(cons):
            if num-1 in cons:
                continue
            temp_num = num
            current = 1
            while temp_num + 1 in cons:
                temp_num = temp_num + 1
                current += 1
            longest = max(longest, current)
        return longest

            

