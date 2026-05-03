class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        arr = [float("inf")] * amount
        for index in range(len(arr)):
            for coin in coins:
                if index + 1 - coin == 0:
                    arr[index] = 1
                elif index + 1 - coin > 0 and arr[index - coin] != float("inf"):
                    arr[index] = min(arr[index], 1 + arr[index-coin])
        if arr[amount-1] == float("inf"):
            return -1
        return arr[amount-1]



                