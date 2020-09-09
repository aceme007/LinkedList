from src.node import Node
from src.llist import SingleLinkedList

llist1 = SingleLinkedList()

def test_SingleLinkedList(llist: SingleLinkedList):
    newNode = Node(data=10)
    llist1.insertNodeAtEnd(newNode=newNode)
    assert llist.get_items() == [10]

    newNode = Node(data=3)
    llist1.insertNodeAtEnd(newNode=newNode)
    assert llist.get_items() == [10, 3]
    assert llist.count == 2
    
    newNode = Node(data="test")
    llist1.insertNodeAtEnd(newNode=newNode)
    assert llist.get_items() == [10, 3, 'test']
    assert llist.count == 3
    print(llist1)

    newNode = Node(data=6)
    llist1.insertNodeAtStart(newNode=newNode)
    assert llist.get_items() == [6, 10, 3, 'test']

    newNode = Node(data="hello")
    llist1.insertNodeAtPosition(newNode=newNode, position=2)
    assert llist.get_items() == [6, 'hello', 10, 3, 'test'], llist1.get_items()
    print(llist1)

    newNode = Node(data="new 1st")
    llist1.insertNodeAtPosition(newNode=newNode, position=1)
    assert llist.get_items() == ['new 1st', 6, 'hello', 10, 3, 'test'], llist1.get_items()
    assert llist.count == 6
    print(llist1)

    llist1.reverse()
    assert llist1.get_items() == ['test', 3, 10, 'hello', 6, 'new 1st'], llist1.get_items()

if __name__ == "__main__":
    test_SingleLinkedList(llist=llist1)

