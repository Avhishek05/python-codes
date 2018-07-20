
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            head = self.head
            while(head.next):
                head=head.next
            head.next = new_node

def getNthFromLast(head, n):
    i=0
    j=0
    while head:
        head=head.next
        i=i+1
        if head==node(n):
            j=i
    return 1



def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(getNthFromLast(head, k))


