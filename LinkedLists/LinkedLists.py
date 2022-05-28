# Create node object
# Create another class to use this node object
# Pass appropriate values through node object to point to next data elements

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedlist:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list1 = SLinkedlist()
list1.headval = Node ("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.headval.nextval = e2

# Link second node to 3rd node

e2.nextval = e3

list1.listprint()



