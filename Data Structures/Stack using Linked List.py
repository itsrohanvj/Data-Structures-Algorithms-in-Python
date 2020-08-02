class Node:
    # constructor
    def __init__(self):
        self.data = None
        self.next = None
        # method for setting the data field of the node

    def set_data(self, data):
        self.data = data

    # method for getting the data field of the node
    def get_data(self):
        return self.data

    # method for setting the next field of the node
    def set_next(self, next):
        self.next = next

    # method for getting the next field of the node
    def get_next(self):
        return self.next

    # returns true if the node points to another node
    def has_next(self):
        return self.next != None


class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    # each element gets inserted into the beginning.
    def push(self, data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head = temp

    # each element gets deleted from the top(beginning).
    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp

# peek to check which element is at the top/head
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.get_data()

    def listLength(self):
        current = self.head
        count = 0
        print("\n Printing Stack\n")
        while current != None:
            count = count + 1
            print(current.get_data())

            current = current.get_next()


our_list = ["first", "second", "third", "fourth", "fifth", "sixth"]
our_stack = Stack(our_list)
print(our_stack.pop())
print(our_stack.peek())
print(our_stack.pop())
print(our_stack.peek())
print(our_stack.pop())
our_stack.listLength()  # to print all the remaining elements in the stack.
