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
        pre = self.head
        data = Node(item)
        for i in range (index-1):
            if pre.next == None:
                print('the index is out of reach')
                return
            pre = pre.next
       
        aft = pre.next
        pre.next = data
        data.next = aft

    def insertatend(self,item):
        temp = self.head
        if self.head == None:
            self.head = Node(item)
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = Node(item)

    def removeitembyobject(self,object):
        if self.head.item == object:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.item != object:
                temp = temp.next
            temp.next = temp.next.next


    def count(self):
        node = self.head
        count = 0
        while node != None:
            node = node.next
            count+=1
        return count



ll=Linkedlist()
ll.insertatbegining(3)
ll.insertatbegining(2)
ll.insertatbegining(1)
ll.insertatbegining(9)
ll.insert(2,5)
ll.insertatend(4)
ll.removeitembyobject(9)
ll.removeitembyobject(2)
print(ll.count())
while ll.head!=None:
    print(ll.head.item)
    ll.head=ll.head.next