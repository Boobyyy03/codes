class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        newNone = None(value)