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


def display(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


if __name__ == "__main__":
    linkedlist = LinkedList()
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)

    head1 = linkedlist.reverseList(head1)
    display(head1)
