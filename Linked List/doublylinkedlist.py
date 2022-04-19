class node:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None
    

class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertatend(self,item):
        newnode = node(item)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
    
    def insertatbegining(self, item):
        newnode = node(item)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def insertafter(self,data, item):
        newnode = node(item)
        if self.head != None:
            temp = self.head
            flag = 0

            while temp != None:
                if temp.data == data:
                    flag = 1
                    break
                temp = temp.next
            
            if flag == 1:
                after = temp.next
                newnode.next = after
                if after != None:
                    after.prev = newnode
                else:
                    self.tail = newnode
                temp.next = newnode
                newnode.prev = temp
            elif flag == 0:
                print(f'{data} not found.')
        else:
            print('list is empty')

    def removekey(self, key):
        if self.head != None:
            temp = self.head
            flag = 0

            while temp != None:
                if temp.data == key:
                    flag = 1
                    break
                temp = temp.next

            if flag == 1:
                if temp == self.head:
                    self.head = temp.next
                else:
                    temp.prev.next = temp.next
                
                if temp == self.tail:
                    self.tail = temp.prev
                else:
                    temp.next.prev = temp.prev
            else:
                print(f'{data} not found.')

    def displayForward(self):
        temp = self.head
        while temp != None:
            print(temp.data, end = ' ')
            temp = temp.next

    def displayBackward(self):
        temp = self.tail
        while temp != None:
            print(temp.data, end =' ')
            temp = temp.prev
        
dll = dll()
dll.insertatbegining(5)
dll.insertatend(13)
dll.insertafter(5,7)
dll.insertafter(7,12)
dll.removekey(13)
dll.displayBackward()