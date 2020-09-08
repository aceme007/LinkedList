class Node:
    def __init__(self, data=None):
        #  --------------
        # | data  | None |
        #  --------------
        if not data:
            raise ValueError('Node cant be init without value/data')
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class SingleLinkedList:
    def __init__(self):
        self.head = None # head points to NULL for empty LL
        self.count = 0

    def __repr__(self):
        current = self.head
        outputList = []
        while current != None:
            outputList.append(current.data)
            current = current.next
        return f"{type(self).__name__} of len : {self.count} having contents : {str(outputList)}"

    def __len__(self):
        return self.count

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

    def inseartNodeAtPosition(self, newNode: Node, position: int):
        assert isinstance(position, int), 'Only integer values allowed for position'
        assert position <= self.count, 'Invalid position for insertion'
        current = self.head
        for i in range(1, position - 1):
            current = current.next
        newNode.next = current.next
        current.next = newNode
        self.count += 1


if __name__ == "__main__":

    l1 = SingleLinkedList()
    l1.insertNodeAtEnd(newNode=Node(data=10))
    print(l1)
    l1.insertNodeAtEnd(newNode=Node(data=3))
    print(l1)
    l1.insertNodeAtEnd(newNode=Node(data="test"))
    print(l1)
    l1.insertNodeAtStart(newNode=Node(data=6))
    print(l1)
    l1.inseartNodeAtPosition(newNode=Node(data="hello"), position=2)
    print(l1)