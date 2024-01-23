
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
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next


if __name__ == "__main__":
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)

    head1 = delete_middle(head1)
    display(head1)
