#This program has an implementation of a binary tree showcasing the different types of tree traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_pre_order(root): 
    """
    Prints a binary tree pre-order
    """

    if root is not None: #Check to make sure root is valid
        print(root.data)
        print_pre_order(root.left)
        print_pre_order(root.right)

def print_in_order(root):
    """
    Prints a binary tree in-order
    """
    if root:
        print_in_order(root.left)
        print(root.data)
        print_in_order(root.right)

def print_post_order(root):
    """
    Prints a binary tree post-order
    """

    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.data)

def main():
#Create a node and insert values
    orange = Node(10)
    orange.left = Node(5)
    orange.right = Node(15)

#Print tree
    print("Tree with values: ")
    print_pre_order(orange)

#Add values
    orange.left.left = Node(3)
    orange.left.right = Node(7)

    orange.right.left = Node(12)
    orange.right.right = Node(20)

#Print tree in-order
    print("\nAfter adding more values:")
    print_in_order(orange)

#Print tree post-order
    print("\nSame tree but printed post-order")
    print_post_order(orange)

#Print tree pre-order
    print("\nSame tree again but printed pre-order")
    print_pre_order(orange)

main()