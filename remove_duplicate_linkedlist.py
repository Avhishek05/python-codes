def removeDuplicates(head):
    if head==None:
        return None
    temp=head
    temp1=head
    while temp.next!=None:
        if temp.data!=temp.next.data:
            temp1.data=temp.data
            temp1=temp1.next
        temp=temp.next
    temp1.data=temp.data
    temp1.next=None
    return head

 
    
class node:
    def __init__(self):
        self.data = None
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
    def get_head(self):
        return self.head
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
def printlist(ptr):
    while ptr!=None:
        print(ptr.data, end=" ")
        ptr= ptr.next
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        newHead = None
        newHead = removeDuplicates(list1.get_head())
        printlist(newHead)
        print('')

