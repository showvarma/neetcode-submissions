class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Stores indices of days waiting for a warmer temperature

        for i, temp in enumerate(temperatures):
            # Resolve all previous days that are cooler than today's temperature
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            
            stack.append(i)

        return res
