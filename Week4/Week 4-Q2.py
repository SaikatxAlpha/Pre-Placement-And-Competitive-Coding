class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def del_head(head):
    if head is None:
        return None
    temp = head
    head = head.next
    if head is not None:
        head.prev = None
    return head
def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
if __name__ == "__main__":
    head = Node(12)
    head.next = Node(22)
    head.next.prev = head
    head.next.next = Node(33)
    head.next.next.prev = head.next
    head = del_head(head)
    print_list(head)