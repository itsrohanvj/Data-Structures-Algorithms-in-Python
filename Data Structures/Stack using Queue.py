class Queue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.queue:
            a = self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError('queue is empty')

    def size(self):
        return len(self.queue)


class Stack(object):
    def __init__(self):
        self.Q1 = Queue()
        self.Q2 = Queue()

    def isEmpty(self):
        return self.Q1.isEmpty() and self.Q2.isEmpty()

    def push(self, item):
        if self.Q2.isEmpty():
            self.Q1.enqueue(item)
        else:
            self.Q2.enqueue(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError('stack is empty')
        elif self.Q2.isEmpty():
            while not self.Q1.isEmpty():
                cur = self.Q1.dequeue()
                if self.Q1.isEmpty():
                    return cur
                self.Q2.enqueue(cur)
        else:
            while not self.Q2.isEmpty():
                cur = self.Q2.dequeue()
                if self.Q2.isEmpty():
                    return cur
                self.Q1.enqueue(cur)


s = Stack()
for i in range(5):  # 0,1,2,3,4
    s.push(i)
for i in range(5):
    print(s.pop())
