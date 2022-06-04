from linked_list import SLinkedList

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def main ():

    my_list = SLinkedList()
    my_list.insertLL(1,1)
    my_list.insertLL(2,1)

    for node in my_list:
        print(node.value)
