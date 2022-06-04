from linked_list import *

# CREATE A NEW INSTANCE OF THE CLASS LINKED LIST
my_list = SLinkedList()

# add some values, each insert at the end of the list using the the 1 value 
my_list.insertLL(1,1)
my_list.insertLL(2,1)
my_list.insertLL(3,1)
my_list.insertLL(4,1)

#I want to insert the value 23 at the begining of the linked list
my_list.insertLL(23,0)

# we choose thelocation : value 15 inserted in at the 3rd position
my_list.insertLL(15,2)

print([node.value for node in my_list])

# TESTING THE TRAVERSE FUNCTION
print("\nTESTING THE TRAVERSE METHOD ")
my_list.traverseSLL()

# TESTING THE SEARSH METHOD
print("\nI AM TESTING THE 'SEARSH METHOD' TO FIND THE ELEMENT WITH THE VALUE '23' IN THE LINKED LIST")
my_list.searchLL(23)
