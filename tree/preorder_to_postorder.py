b=[]
def postorder(root):
    if root==None:
        return
    postorder(root.left)
    #print(root.data,end=" ")
    postorder(root.right)
    b.append(root.data)

def preordertoposorder(a,n):
    root=Node(a[0])
    stack=[]
    stack.append(root)
    temp=None
    for i in range(1,len(a)):

        while len(stack)!=0 and a[i]>stack[-1].data:
            temp=stack.pop()
        if temp!=None:
            temp.right=Node(a[i])
            stack.append(temp.right)
        else:
            stack[-1].left=Node(a[i])
            stack.append(stack[-1].left)
    return root
# z=int(input())   for geeksforgeeks input
# for i in range(z):
#     n=int(input())
#     a=list(map(int,input().split()))
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None  


a=[7,40, 30, 28, 35, 80, 70, 100]
n=5
root=preordertoposorder(a,n)
postorder(root)
if len(b)!=len(a):
    print("NO")
    print(*b)
else:
    print(*b)
# print(root.data)
# print(root.left.data)
# print(root.right.data)
# print(root.left.right.data)
# print(root.right.right.data)
    