#This program has a basic implementation of a binary search tree
#with a print function that traverses a tree pre-order

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,data):
        if data >= self.data and self.right is not None: #If the data is greater than or equal to the current node, put it on the right
            self.right.insert(data)
        
        if data < self.data and self.left is not None: #If the data is less than the current node, put it on the left
            self.left.insert(data)
        
        if self.right is None and data >= self.data:
            self.right = Node(data)
        
        if self.left is None and data < self.data:
            self.left = Node(data)
    
    def print_pre_order(self):
        if self is not None:
            print(self.data, end=" ") #Visit root first

            if self.left is not None:
                self.left.print_pre_order() #Then left child
            
            if self.right is not None:
                self.right.print_pre_order() #Then right child
    
    def print(self):
        self.print_pre_order()
        print("")
            

def main():
#Create apple tree
    apple = Node(10)
    print("Insert 10: ")
    apple.print()

    print("\nAfter inserting 5 and 15: ")

#Insert 5 and 15 and print
    apple.insert(5)
    apple.insert(15)
    apple.print()

#Insert 3, 20, 11
    apple.insert(3)
    apple.insert(20)
    apple.insert(11)

    print("\nAfter inserting 3, 20, and 11")
    apple.print()

    print("apple.left.data =",apple.left.data)
    print("apple.right.data =",apple.right.data)

    print("apple.left.left.data =",apple.left.left.data)


main()

