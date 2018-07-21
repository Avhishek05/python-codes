from collections import deque
def bottom_view(root):
    if root==None:
        return
    q=deque()
    bottomview={}
    q.append((root,0))
    while q:
        elem,hd=q.popleft()
        bottomview[hd]=elem.data
        if elem.left is not None:
            q.append((elem.left,hd-1))
        if elem.right is not None:
            q.append((elem.right,hd+1))
    return bottomview


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(7)
root.left.right = Node(5)
root.right.left = Node(6)
bottomview=bottom_view(root)
for i in sorted(bottomview):
    print(bottomview[i], end=' ')
