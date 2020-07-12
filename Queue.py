# QUEUE WORKS AS 'FIFO'.

class Queue(object):
    def __init__(self, limit = 10):
        self.que = []  #Empty list
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    def isEmpty(self):
        return self.size < 0
    #EnQueue - inserting values in Queue
    def enQueue(self, item):
        if self.size >= self.limit:
            print ('Queue Overflow!')
            return
        else:
            self.que.append(item)
        if self.front is None:
            self.front = self.rear= 0
        else:
            self.rear = self.size
        self.size += 1
        print ('Queue after enQueue',self.que)
# deQueue - popping out values from Queue.        
    def deQueue(self):
        if self.size <= 0:
            print ('Queue Underflow')
            return 0
        else:
            self.que.pop(0)
            self.size-=1
            if self.size == 0:
                self.front= self.rear =None
            else:
                self.rear = self.size-1
            print ('Queue after deQueue',self.que)
    def queueRear(self):
        if self.rear is None:
            print ("Sorry, the queue is empty!")
            raise lndexError
        return self.que[self.rear]
    def queueFront(self):
        if self.front is None:
            print ("Sorry, the queue is empty!")
            raise lndexError
        return self.que[self. front]
    def size(self):
        return self.size  
    
#Calling the functions and inserting values.    

que = Queue()
#pushing values in Queue
que.enQueue("first")
print ("Front: "+que.queueFront())
print ("Rear: "+que.queueRear())

que.enQueue("second")
print ("Front: "+que.queueFront())
print ("Rear: "+que.queueRear())

que.enQueue("third")
print ("Front: "+que.queueFront())
print ("Rear: " +que.queueRear())

#poping out values fro Queue.
que.deQueue()
print ("Front: "+que.queueFront())
print ("Rear: "+que.queueRear())

que.deQueue()
print ("f'ront: "+que.queueFront())
print ("Rear: "+que.queueRear())

