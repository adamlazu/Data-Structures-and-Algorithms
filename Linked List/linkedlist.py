class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
# for creating the node that contains the data and a pointer to point into another nodes

class Linkedlist:
    def __init__(self):
        self.head = None
    #pointing at the begining of the first node

    def insertatbegining(self, item):
        temp = self.head
        self.head = Node(item)
        self.head.next = temp
    #inserting nodes at the begining of linked list (can be used to implement a stack)

    def insert(self, index, item):
        flag = 1
        pre = self.head
        data = Node(item)
        for i in range (index-1):
            if pre.next == None:
                print('the index is out of reach')
                flag = 0
            pre = pre.next
        if flag == 1:
            aft = pre.next
            pre.next = data
            data.next = aft
        else:
            pass




ll=Linkedlist()
ll.insertatbegining(3)
ll.insertatbegining(2)
ll.insertatbegining(1)
ll.insert(2,5)
while ll.head!=None:
    print(ll.head.item)
    ll.head=ll.head.next