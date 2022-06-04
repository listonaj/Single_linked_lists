from linked_list import *

my_list = SLinkedList()
# add some values, each insert at the end of the list using the the 1 value 
my_list.insertLL(1,1)
my_list.insertLL(2,1)
my_list.insertLL(3,1)
my_list.insertLL(4,1)

#I want to insert the value 23 at the begining of the linked list
my_list.insertLL(23,0)

print([node.value for node in my_list])