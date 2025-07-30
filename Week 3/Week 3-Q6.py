class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
def detectLoop(head):
    st = set()
    while head is not None:
        if head in st:
            return True
        st.add(head)
        head = head.next
    return False
if __name__ == "__main__":
    head = Node(7845)
    head.next = Node(7458)
    head.next.next = Node(44578)
    head.next.next.next = head.next
    if detectLoop(head):
        print("Loop detected")
    else:
        print("Loop not found")