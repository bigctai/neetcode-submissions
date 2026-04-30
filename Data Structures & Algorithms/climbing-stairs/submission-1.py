class Solution:
    def climbStairs(self, n: int) -> int:
        count = []
        for i in range(n):
            if i == 0:
                count.append(1)
            elif i == 1:
                count.append(2)
            else:
                count.append(count[i-1]+count[i-2])
        return count[n-1]
