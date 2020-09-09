from .node import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None # head points to NULL for empty LL
        self.count = 0

    def __repr__(self):
        return f"{type(self).__name__} of len : {self.count} having contents : {str(self.get_items())}"

    def __len__(self):
        return self.count

    def get_items(self) -> list:
        'return all items in SingleLinkedList'
        current = self.head
        outputList = []
<<<<<<< HEAD:src/llist.py
        while current: # != None
=======
        while current != None:
>>>>>>> 91a69b0f3040232e26ca72d55eca05837e1a9d47:src/llist.py
            outputList.append(current.data)
            current = current.next
        return outputList
    
    def insertNodeAtEnd(self, newNode: Node):
        if self.head == None: # no node present in LL
            self.head = newNode
        else:
            # traverse LL 1st
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
        self.count += 1

    def insertNodeAtStart(self, newNode: Node):
        newNode.next = self.head
        self.head = newNode
        self.count += 1

    def insertNodeAtPosition(self, newNode: Node, position: int):
        assert isinstance(position, int), 'Only integer values allowed for position'
        assert position >= 1, 'Invalid position. 1st position in list is 1'
        assert position <= self.count, 'Invalid position for insertion'
        if position == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            for i in range(1, position - 1):
                current = current.next
            newNode.next = current.next
            current.next = newNode
        self.count += 1

    def reverse(self):
        current = self.head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous
