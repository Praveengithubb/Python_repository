from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


@staticmethod
def recent_counter(commands, parameters):
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


def main():
    commands = ["RecentCounter", "ping", "ping", "ping", "ping"]
    parameters = [[], [1], [100], [3001], [3002]]
    result = recent_counter(commands, parameters)

    for res in result:
        print(res, end=" ")


if __name__ == "__main__":
    main()
