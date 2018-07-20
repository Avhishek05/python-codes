class Node:
    def __init__(self, data):
        data = data
        next = None
class LinkedList:
    def __init__(self):
        head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = head
        head = new_node
    def printList(self):
        temp = head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1

def reverse(head, k):
    if k==1:
        return head
    if head.next==None:
        return head
    first=head
    temp1=head
    prev = None
    flag = False
    while temp1.next:
        if k == 0 :
            flag = True
            prev.next = None 
            head = temp1
        prev=temp1
        temp1=temp1.next
        k-=1
    if k == 0:
        flag = True
        prev.next = None 
        head = temp1
    if flag:
        temp1.next=first
        temp=head

        
    i=0
    while temp:
        temp=temp.next
        i=i+1


    prev=None
    current=head
    next = current.next
    while i//2!= 0:
        next = current.next
        current.next = prev
        prev = current
        current = next
        i=i-1
    next.next = prev
    head = next
    return
