class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insertLL(self, value, location):
            newNode = Node(value)
            #1) case where the list is empty
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            #2) case where we insert in the first position in the list
            else:
                if location == 0:
                    newNode.next = self.head
                    self.head = newNode
            #3) case where we insert in the last position in the list
                elif location == 1:
                    newNode.next = None
                    self.tail.next = newNode
                    self.tail = newNode
            #4) insert in the middle of the list
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
                    if tempNode == self.tail:
                        self.tail=newNode
                        
    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

    #  Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None
    
