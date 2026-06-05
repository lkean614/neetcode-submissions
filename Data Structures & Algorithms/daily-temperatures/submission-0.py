class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for index,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_temp = stack.pop()
                res[prev_temp] = index - prev_temp
            stack.append(index)
        return res