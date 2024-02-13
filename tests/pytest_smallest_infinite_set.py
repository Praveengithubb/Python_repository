import unittest


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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        set_instance = SmallestInfiniteSet()
        set_instance.add_back(5)
        self.assertEqual(1, set_instance.pop_smallest())  # add assertion here

    def test_something1(self):
        set_instance = SmallestInfiniteSet()
        set_instance.add_back(1)
        set_instance.pop_smallest()
        self.assertEqual(2, set_instance.pop_smallest())


if __name__ == '__main__':
    unittest.main()
