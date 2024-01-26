import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def pair_sum(head):
    slow = head
    fast = head
    max_val = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    next_node = None
    prev = None
    while slow is not None:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    while prev is not None:
        max_val = max(max_val, head.val + prev.val)
        prev = prev.next
        head = head.next
    return max_val


class MyTestCase(unittest.TestCase):
    def test_something(self):
        head1 = Node(5)
        head1.next = Node(4)
        head1.next.next = Node(3)
        head1.next.next.next = Node(2)
        head1.next.next.next.next = Node(1)

        max = pair_sum(head1)
        res = 6
        self.assertEqual(max, res)

    def test_something1(self):
        head1 = Node(4)
        head1.next = Node(2)
        head1.next.next = Node(2)
        head1.next.next.next = Node(3)

        max = pair_sum(head1)
        res = 7
        self.assertEqual(max, res)

    def test_something2(self):
        head1 = Node(1)
        head1.next = Node(200)

        max = pair_sum(head1)
        res = 201
        self.assertEqual(max, res)


if __name__ == '__main__':
    unittest.main()
