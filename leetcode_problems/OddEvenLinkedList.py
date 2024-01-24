from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def oddEvenList(self, head: Optional[Node]) -> Optional[Node]:
        odd_head, odd_tail, even_head, even_tail = None, None, None, None
        count = 1
        while head:
            if count % 2 == 0:
                if even_head is None:
                    even_head = head
                    even_tail = head
                    head = head.next
                else:
                    even_tail.next = head
                    even_tail = even_tail.next
                    head = head.next
            else:
                if odd_head is None:
                    odd_head = head
                    odd_tail = head
                    head = head.next
                else:
                    odd_tail.next = head
                    odd_tail = odd_tail.next
                    head = head.next
            count += 1
        if odd_head is None:
            return even_head
        if even_head is None:
            return odd_head
        even_tail.next = None
        odd_tail.next = even_head
        return odd_head

    def display(self, head):
        current = head
        while current:
            print(current.val, end=" ")
            current = current.next


if __name__ == "__main__":
    linked_list = LinkedList()

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)

    head1 = linked_list.oddEvenList(head1)
    linked_list.display(head1)
