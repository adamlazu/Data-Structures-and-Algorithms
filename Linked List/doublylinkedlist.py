class node:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None
    

class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertatand(self,item):
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


dll = dll()

dll.insertatand(2)
dll.insertafter(2,4)
dll.insertafter(4,8)
dll.insertafter(2,3)

print(dll.head.next.data)