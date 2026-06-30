class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIdx, stackTemp = stack.pop()
                result[stackIdx] = i - stackIdx
            stack.append((i, temp))

        return result
