class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self , data):
        if self.data:
            if data < self.left:
                if self.left is None:
                    self.left = Node(data)
                else :
                    self.left.insert(data)
            elif data > self.right:
                if self.right is None:
                    self.right = Node(data)
                else :
                    self.right.insert(data)
        else :
            self.data = data

#         def printtree(self):
#             if self.left:
#                 self.left.printtree()
#             print(self.data),
#             if self.right:
#                 self.right.printtree()
#
# root = Node(10)
# root.insert(3)
# root.insert(24)
# root.insert(5)
# root.insert(34)
#
# root.printtree()
# Print the tree

    def findval(self, val):
        if val < self.data:
            if self.left is None:
                return "value not found"
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return "value not found"
            return self.right.findval(val)
        else :
            print (str(self.data)+ "  value found")


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()




# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.findval(12)
root.PrintTree()
