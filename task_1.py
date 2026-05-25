class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        return " -> ".join(str(x) for x in self.to_list())


def reverse(ll):
    prev = None
    current = ll.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    ll.head = prev
    return ll


def merge_sort(ll):
    if ll.head is None or ll.head.next is None:
        return ll

    left_head, right_head = split(ll.head)

    left = LinkedList()
    left.head = left_head
    right = LinkedList()
    right.head = right_head

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def split(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return head, mid


def merge(left, right):
    dummy = Node(0)
    current = dummy
    l, r = left.head, right.head
    while l and r:
        if l.data <= r.data:
            current.next = l
            l = l.next
        else:
            current.next = r
            r = r.next
        current = current.next
    current.next = l or r
    result = LinkedList()
    result.head = dummy.next
    return result


def merge_two_sorted(ll1, ll2):
    return merge(ll1, ll2)


if __name__ == "__main__":
    ll = LinkedList()
    for val in [3, 1, 4, 1, 5, 9, 2, 6]:
        ll.append(val)

    print("Оригінал:  ", ll)
    print("Реверс:    ", reverse(ll))

    ll2 = LinkedList()
    for val in [3, 1, 4, 1, 5, 9, 2, 6]:
        ll2.append(val)
    print("Сортування:", merge_sort(ll2))

    ll3, ll4 = LinkedList(), LinkedList()
    for val in [1, 3, 5]: ll3.append(val)
    for val in [2, 4, 6]: ll4.append(val)
    print("Об'єднання:", merge_two_sorted(ll3, ll4))
