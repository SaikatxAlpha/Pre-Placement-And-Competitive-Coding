class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
def search_key(head, key):
    curr = head
    while curr is not None:
        if curr.data == key:
            return True
        curr = curr.next
    return False
if __name__ == "__main__":
    head = Node(114)
    head.next = Node(121)
    head.next.next = Node(153)
    head.next.next.next = Node(3880)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(990)
    key = 990
    if search_key(head, key):
        print("Founded")
    else:
        print("Not found")