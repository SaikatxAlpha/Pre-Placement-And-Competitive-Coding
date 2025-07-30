class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def deleteNode(self, key):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp is None:
            return
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
llist = LinkedList()
for val in [70, 1011, 30, 254]:
    llist.push(val)
print("Original Linkedlist:")
llist.printList()
llist.deleteNode(1011)
print("Linked List after 1011:")
llist.printList()


# Original Linkedlist:
# 254 30 1011 70 
# Linked List after 1011:   
# 254 30 70 
