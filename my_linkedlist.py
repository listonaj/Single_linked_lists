from linked_list import *

# CREATE A NEW INSTANCE OF THE CLASS LINKED LIST
my_list = SLinkedList()

# INSERTING SOME ELEMENTS IN THE LIST 
my_list.insertLL(1,1)
my_list.insertLL(2,1)
my_list.insertLL(3,1)
my_list.insertLL(4,1)

#I want to insert the value 23 at the beginning of the linked list
my_list.insertLL(23,0)

# we choose the position of the node: value 15 inserted in at the 3rd position
my_list.insertLL(15,2)
print("AFTER HAVING INSERTED SOME ELEMENTS IN THE LINKED LIST, I PRINT ITS CONTENT")
print([node.value for node in my_list])

# TESTING THE TRAVERSE FUNCTION
print("\nTESTING THE TRAVERSE METHOD ")
my_list.traverseSLL()

# TESTING THE SEARSH METHOD
print("\nI AM TESTING THE 'SEARSH METHOD' TO FIND THE ELEMENT WITH THE VALUE '23' IN THE LINKED LIST")
my_list.searchLL(23)
