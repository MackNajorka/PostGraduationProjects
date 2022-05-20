# Program to convert a binary 
# tree to its mirror

# Utility function to create a new
# tree node
class newNode:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

""" Change a tree so that the roles of the
    left and right pointers are swapped at
    every node.
 
So the tree...
     4
    / \
   2   5
  / \
 1   3
 
is changed to...
    4
   / \
  5   2
     / \
    3   1
"""

def mirror(node):
    
    if (node == None):
        return
    else:
        temp = node

        # sub trees
        mirror(node.left)
        mirror(node.right)

        # swap the pointers in this node
        temp= node.left
        node.left = node.right
        node.right = temp

#function to print inOrder traversal
def inOrder(node):

    if (node == None):
        return

    inOrder(node.left)
    print(node.data, end = " ")
    inOrder(node.right)

# Driver code
if __name__ == "__main__":

    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.right.right = newNode(5)

    #print inorder traversal of the input tree
    print("Inorder traversal of the constructed tree is ")

    inOrder(root)

    # convert tree to its mirror

    mirror(root)

    print("\n Inorder traversal of the mirror tree is ")
    inOrder(root)