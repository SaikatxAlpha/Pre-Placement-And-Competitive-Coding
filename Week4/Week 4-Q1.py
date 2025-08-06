class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None
def insert_at_front(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node
def print_list(head):
    curr = head
    while curr is not None:
        print(f" {curr.data}", end='')
        curr = curr.next
    print()  
if __name__ == "__main__":
    head = Node(2.2)
    head.next = Node(3.56)
    head.next.prev = head
    head.next.next = Node(4.22)
    head.next.next.prev = head.next
    print("Original Linked List:", end='')
    print_list(head)
    print("After inserting Node at the front:", end='')
    data = 1.0215
    head = insert_at_front(head, data)
    print_list(head)

#Original Linked List: 2.2 3.56 4.22
#After inserting Node at the front: 1.0215 2.2 3.56 4.22
