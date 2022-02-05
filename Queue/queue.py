#this is a queue implementation in python
class queue:
    def __init__(self):
        self.queue = []
        #this creates an empty list that will be used as a queue
    
    def enqueue(self, item):
        return self.queue.append(item)
        #this method will add an item into the queue
    
    def dequeue(self):
        if len(self.queue)!=0:
            return self.queue.pop(0)
        else:
            print("the queue is already empty!")
        #this returns an item at the front of the queue and also removes it
    
    def peek(self):
        return self.queue[0]
        #this returns the item at the front of queue without removing it

queue = queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

while len(queue.queue)!=0:
    print(queue.dequeue())