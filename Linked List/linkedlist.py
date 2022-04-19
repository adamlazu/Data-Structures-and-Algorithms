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
        #inserting an item at certain index

    def insertatend(self,item):
        temp = self.head
        if self.head == None:
            self.head = Node(item)
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = Node(item)
        #inserting item at the end of linked list

    def removeitembyobject(self,object):
        if self.head.item == object:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.item != object:
                temp = temp.next
            temp.next = temp.next.next
        #removing item by the object
    
    def search(self, object):
        temp = self.head
        while temp != None:
            if temp.item == object:
                return True
            temp = temp.next
        return False
        #searching item

    def count(self):
        node = self.head
        count = 0
        while node != None:
            node = node.next
            count+=1
        return count
        #count the nodes
    
    def reverse(self):
        prev = None
        curr = self.head
        after = None

        while curr != None:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        self.head = prev

    def printlist(self):
        temp = self.head
        while temp != None:
            print(temp.item, end = ' ')
            temp = temp.next
            


ll=Linkedlist()
ll.insertatbegining(3)
ll.insertatbegining(2)
ll.insertatbegining(1)
ll.insertatbegining(9)
ll.insert(2,5)
ll.insertatend(4)
ll.reverse()
ll.printlist()
