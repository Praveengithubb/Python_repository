class SmallestInfiniteSet:
    def __init__(self):
        self.curr = 1
        self.s = set()

    def pop_smallest(self):
        if self.s:
            res = min(self.s)
            self.s.remove(res)
            return res
        else:
            self.curr += 1
            return self.curr - 1

    def add_back(self, num):
        if num < self.curr:
            self.s.add(num)


if __name__ == "__main__":
    set_instance = SmallestInfiniteSet()
    print(set_instance.pop_smallest())
    set_instance.add_back(2)
    print(set_instance.pop_smallest())
    print(set_instance.pop_smallest())
    print(set_instance.pop_smallest())
    set_instance.add_back(1)
    print(set_instance.pop_smallest())
    print(set_instance.pop_smallest())
