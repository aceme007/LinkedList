class Node:
    def __init__(self, data=None):
        #  --------------
        # | data  | None |
        #  --------------
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None # head points to NULL for empty LL

    def printLinkedList(self):
        current = self.head
        print(f"{type(self).__name__} contents :")
        while current != None:
            print(f"{current.data}")
            current = current.next
        print("\n")

    def insertNodeAtEnd(self, newNode: Node):
        if self.head == None: # no node present in LL
            self.head = newNode
        else:
            # traverse LL 1st
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode

    def insertNodeAtStart(self, newNode: Node):
        newNode.next = self.head
        self.head = newNode


if __name__ == "__main__":
    ll = SingleLinkedList()
    ll.insertNodeAtEnd(Node(data=10))
    ll.printLinkedList()
    ll.insertNodeAtEnd(Node(data=3))
    ll.printLinkedList()
    ll.insertNodeAtEnd(Node(data=33))
    ll.printLinkedList()
    ll.insertNodeAtStart(Node(data=6))
    ll.printLinkedList()