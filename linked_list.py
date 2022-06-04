from SinglLinkedList import Node
from SinglLinkedList import SLinkedList

def main():

    print("this is the main function for the linked list")
    my_linkedlist = SLinkedList()

    # CREATE TWO NODE
    node1 = Node(1)
    node2 = Node(2)

    # SPECIFY THE POSITION OF THE TWO NODES CREATED IN LINE 9
    my_linkedlist.head = node1
    my_linkedlist.next = node2
    my_linkedlist.tail = node2

    
    

    

    
