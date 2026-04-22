class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_diff = 0
        for price in prices:
            if price <= minimum:
                minimum = price
                continue
            diff = price - minimum
            max_diff = max(diff, max_diff)
        return max_diff