from SinglLinkedList import Node
from SinglLinkedList import SLinkedList

def main():

    print("this is the main function for the linked list")
    singlLinkedList = SLinkedList()
    singlLinkedList.insertSLL(44,6)
    print([node.value for node in singlLinkedList]) 

    node1 = Node(1)
    node2 = Node(2)

    singlLinkedList.head = node1
    singlLinkedList.head.next = node2
    singlLinkedList.tail = node2

    singlLinkedList.insertSLL(3,1)
    singlLinkedList.insertSLL(4,1)
    print([node.value for node in singlLinkedList]) 
    singlLinkedList.insertSLL(5,3)
    print([node.value for node in singlLinkedList]) 

    singlLinkedList = SLinkedList()
    # singlLinkedList.insertSLL(1, 1)
    # singlLinkedList.insertSLL(2, 3)
    # singlLinkedList.insertSLL(3, 1)
    # singlLinkedList.insertSLL(4, 1)
    # singlLinkedList.insertSLL(0, 0)
    # singlLinkedList.insertSLL(7, -1)
    # singlLinkedList.insertSLL(5, 6)


    # singlLinkedList.insertSLL(1,1)
    # singlLinkedList.insertSLL(2,5)
    # singlLinkedList.insertSLL(3,1)
    # singlLinkedList.insertSLL(4,9)
    # singlLinkedList.insertSLL(5,-1)
    singlLinkedList.insertSLL(1, 1)
    singlLinkedList.insertSLL(2, 1)
    singlLinkedList.insertSLL(3, 1)
    singlLinkedList.insertSLL(4, 1)
    singlLinkedList.insertSLL(5,-1)

    print([node.value for node in singlLinkedList]) 
    singlLinkedList.deleteEntireSLL()
    print([node.value for node in singlLinkedList]) 

