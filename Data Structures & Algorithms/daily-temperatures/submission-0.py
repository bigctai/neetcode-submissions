class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1]["temp"] < temp:
                ind = stack.pop()["index"]
                res[ind] = i - ind
            stack.append({"index": i, "temp": temp})
        return res
