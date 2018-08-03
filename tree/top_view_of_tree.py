class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def findminmax(root,minimum,maximum,hd):
	if root is None:
		return
	if hd<minimum[0]:
		minimum[0]=hd
	elif hd>maximum[0]:
		maximum[0]=hd
	findminmax(root.left,minimum,maximum,hd-1)
	findminmax(root.right,minimum,maximum,hd+1)

def printverticle(root,lineno,hd):
	if root is None:
		return
	if hd==lineno:
		print(root.data,end=" ")
		return
		

	printverticle(root.left,lineno,hd-1)
	printverticle(root.right,lineno,hd+1)

def verticleorder(root):
	minimum=[0]
	maximum=[0]
	findminmax(root,minimum,maximum,0)
	for lineno in range(minimum[0],maximum[0]+1):
		printverticle(root,lineno,0)
		print("")

root = Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.left.right=Node(8)
root.right.right.right=Node(9)
verticleorder(root)