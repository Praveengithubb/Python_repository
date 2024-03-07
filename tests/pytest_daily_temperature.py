import unittest


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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Temp()
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        self.assertEqual([1, 1, 4, 2, 1, 1, 0, 0], s.dailyTemperatures(temperatures))  # add assertion here

    def test_something1(self):
        s = Temp()
        temperatures = [30, 40, 50, 60]
        self.assertEqual([1, 1, 1, 0], s.dailyTemperatures(temperatures))


if __name__ == '__main__':
    unittest.main()
