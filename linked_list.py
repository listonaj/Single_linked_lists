from SinglLinkedList import Node
from SinglLinkedList import SLinkedList

def main():

    print("this is the main function for the linked list")
    singlyLinkedList = SLinkedList()
    singlyLinkedList.insertSLL(44,6)
    print([node.value for node in singlyLinkedList]) 

    # node1 = Node(1)
    # node2 = Node(2)

    # singlyLinkedList.head = node1
    # singlyLinkedList.head.next = node2
    # singlyLinkedList.tail = node2

    singlyLinkedList.insertSLL(3,1)
    singlyLinkedList.insertSLL(4,1)
    print([node.value for node in singlyLinkedList]) 
    singlyLinkedList.insertSLL(5,3)
    print([node.value for node in singlyLinkedList]) 

