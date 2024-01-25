import unittest

from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def reverseList(self, head: Node) -> Node:
        neww = None
        prev = None
        while head is not None:
            neww = head.next
            head.next = prev
            prev = head
            head = neww
        return prev


class MyTestCase(unittest.TestCase):
    def test_something(self):
        linked_list = LinkedList()
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(3)
        head1.next.next.next = Node(4)
        head1.next.next.next.next = Node(5)

        head1 = linked_list.reverseList(head1)
        actual_result = []
        current = head1
        while current:
            actual_result.append(current.val)
            current = current.next
        excepted_result = [5, 4, 3, 2, 1]
        self.assertEqual(actual_result, excepted_result)

    def test_something1(self):
        linked_list = LinkedList()
        head1 = Node(1)
        head1.next = Node(2)

        head1 = linked_list.reverseList(head1)
        actual_result = []
        current = head1
        while current:
            actual_result.append(current.val)
            current = current.next

        expected_result = [2, 1]
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
