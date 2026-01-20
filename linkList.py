#  Linked List 
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None
        
#created Seperate Nodes     
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Linking of all nodes 
head.next = node2
node2.next = node3 
node3.next = node4 
node4.next = node5 

# Print Nodes
print("Current link list is=")

currentnode = head 
while currentnode is not None: 
    print(currentnode.data, end="=>")
    currentnode=currentnode.next 
print("None")

# o/p = Current link list is=
# 10=>20=>30=>40=>50=>None
# task = add and remove element.

