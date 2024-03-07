class Temp:
    def dailyTemperatures(self, temps):
        results = [0] * len(temps)
        stack = []
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)
        return results


s = Temp()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(temperatures))
