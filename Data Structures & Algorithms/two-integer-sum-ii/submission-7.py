class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffs = {}
        for index, num in enumerate(numbers, 1):
            diffs[target-num] = index
        for index, num in enumerate(numbers, 1):
            if num in diffs and num!=numbers[diffs[num]-1]:
                return [index, diffs[num]]
