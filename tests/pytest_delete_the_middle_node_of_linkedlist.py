import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def delete_middle(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head.next.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next

    return head


def display(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        print(current.val, end=" ")
        current = current.next
    return result


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        # Test case 1: Normal case with an odd number of nodes
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(3)
        head1.next.next.next = Node(4)
        head1.next.next.next.next = Node(5)

        delete_middle(head1)
        self.assertEqual(display(head1), [1, 2, 4, 5])

    def test_something2(self):
        # Test case 1: Normal case with an odd number of nodes
        head1 = Node(1)
        head1.next = Node(2)

        delete_middle(head1)
        self.assertEqual(display(head1), [1])

    def test_something3(self):
        # Test case 1: Normal case with an odd number of nodes
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(3)
        head1.next.next.next = Node(4)

        delete_middle(head1)
        self.assertEqual(display(head1), [1, 2, 4])


if __name__ == '__main__':
    unittest.main()
