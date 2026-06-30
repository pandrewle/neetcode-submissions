class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idx_dict = {}
        i = len(temperatures)-1
        result = [0] * len(temperatures)
        stack = []
        while i >= 0:
            print(stack)
            print(result)
            currentTemp = temperatures[i]
            idx_dict[currentTemp] = i
            while stack and currentTemp >= stack[-1]:
                stack.pop()
            if stack and currentTemp < stack[-1]:
                result[i] = idx_dict[stack[-1]] - i
            else:
                print(i)
                result[i] = 0

            stack.append(currentTemp)
            i -= 1

        return result
