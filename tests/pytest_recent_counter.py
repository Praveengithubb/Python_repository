import unittest
from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

    def recent_counter(self, commands, parameters):
        result = []
        recent_counter_instance = None

        for i in range(len(commands)):
            command = commands[i]

            if command == "RecentCounter":
                recent_counter_instance = RecentCounter()
                result.append(None)
            elif command == "ping":
                if recent_counter_instance:
                    result.append(recent_counter_instance.ping(parameters[i][0]))

        return result


class MyTestCase(unittest.TestCase):
    def test1(self):
        commands = ["RecentCounter", "ping", "ping", "ping", "ping"]
        parameters = [[], [1], [100], [3001], [3002]]
        counter = RecentCounter()
        result = counter.recent_counter(commands, parameters)
        self.assertEqual(result, [None, 1, 2, 3, 3])

    def test2(self):
        commands = ["RecentCounter", "ping", "ping", "ping", "ping", "ping"]
        parameters = [[], [1], [100], [3001], [3002], [4000]]
        counter = RecentCounter()
        result = counter.recent_counter(commands, parameters)
        self.assertEqual(result, [None, 1, 2, 3, 3, 3])

    def test3(self):
        commands = ["RecentCounter", "ping", "ping", "ping", "ping", "ping", "ping"]
        parameters = [[], [1], [100], [3001], [3002], [4000], [5000]]
        counter = RecentCounter()
        result = counter.recent_counter(commands, parameters)
        self.assertEqual(result, [None, 1, 2, 3, 3, 3, 4])


if __name__ == '__main__':
    unittest.main()
