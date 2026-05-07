class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        num1, num2 = cost[-1], cost[-2]
        for i in range(3, len(cost)+1, 1):
            temp = cost[-i] + min(num1, num2)
            num1 = num2
            num2 = temp
        return min(num1, num2)