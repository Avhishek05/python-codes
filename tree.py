class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
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


    #
    # def insert(self , data):
    #     if self.data:
    #         if data < self.left:
    #             if self.left is None:
    #                 self.left = Node(data)
    #             else :
    #                 self.left.insert(data)
    #         elif data > self.right:
    #             if self.right is None:
    #                 self.right = Node(data)
    #             else :
    #                 self.right.insert(data)
    #     else :
    #         self.data = data















    def PrintTree(self):
            if self.left:
                self.left.PrintTree()
            print (self.data),
            if self.right:
                self.right.PrintTree()


root = Node(15)
root.insert(5)
root.insert(2)
root.insert(17)
root.insert(19)
root.PrintTree()
print (root.right.data)
