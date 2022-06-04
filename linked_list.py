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
    
    # the method take two parameter the value and the location ever 0 or 1 or none 
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

    # Traverse the linked list
    def traverseSLL(self):
        # no head in the list  -> means no list 
        if self.head is None:
            print("The Singly Linked List does not exist")
        # we can traverse 
        else:
            # we create a temp node that we evaluate being the head
            node = self.head
            # if it is none means we arrive at the end of the list
            while node is not None:
                # we print the value of the node 
                print(node.value)
                # we iterate in the linked list using next
                node = node.next

    # Searching method to look for a node in a Linked List.
    # the method take one parameter(beside self) which is... 
    # the value we are looking for 
    def searchLL(self, nodeValue):
        # again we check the head value because if there... 
        # is no head, there is no list
        if self.head is None:
           return "no list have been created, Sorry !"
        else:
            # we create a dummy node called 'nodeValue'. that node will take... 
            # the value we are looking for.
            # we will compare the value of that dummy node with each element... 
            # in the list until the value matches.

            # we start at the head of the list 
            node = self.head
            # looping as long as we are not arrive at the end of the list
            while node is not None:
                # values matches  - we use double equal for comparing elemnents
                if node.value == nodeValue:
                    print(f"Great news! I have found the value '{node.value}' in the linked list\n")
                    return node.value
                # we iterate in the list using next if we have not found the value yet
                node = node.next
            # if after traversing all the list tghe value is not found,
            # we print a statement that says so.
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
    
