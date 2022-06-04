from linked_list import *

my_list = SLinkedList()
my_list.insertLL(1,1)
my_list.insertLL(2,1)
my_list.insertLL(2,1)
my_list.insertLL(2,1)

for node in my_list:
    print(node.value)
