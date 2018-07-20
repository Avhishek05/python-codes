class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printancestor(root,target):
    if root==None:
        return True
    if root.data==target:
        return True
    if (printancestor(root.left,target)or printancestor(root.right,target)):
        print (root.data, end=" ")
        return True
    return False


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(7)
printancestor(root,7)
