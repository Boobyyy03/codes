class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def front(self):
        if self.head is None:
            return -1
        else:
            return self.head.val

    def dequeue(self):
        if self.head is None:
            return -1
        else:
            tempNode = self.head
            self.head = self.head.next
            self.length -= 1
            return tempNode.val

    def isEmpty(self):
        return not(bool(self.length))

    def size(self):
        return self.length

    def clear(self):
        self.head = self.tail = None

    def display(self):
        if self.head != None:
            print("Elements in stack:", end=" ")
            tmpNode = self.head
            while tmpNode is not None:
                print (tmpNode.val, end= " ")
                tmpNode = tmpNode.next
            print()
        else:
            print("Empty!");

def menu(queue):
    while(True):
        print ("+----------------MENU--------------+")
        print ("|   0.Quit.                        |")
        print ("|   1.Enqueue.                     |")
        print ("|   2.Dequeue.                     |")
        print ("|   3.Front.                       |")
        print ("|   4.Is Empty.                    |")
        print ("|   5.Size.                        |")
        print ("|   6.Check queue.                 |")
        print ("|   7.Clear.                       |")
        print ("+----------------------------------+")

        choose = int(input("Input number: "))
        if choose == 0:
            print ("Done!")
            break
        elif choose == 1:
            val = int(input("Input value: "))
            queue.enqueue(val)
        elif choose == 2:
            tmp = queue.dequeue()
            if tmp != -1: print ("First element:",tmp)
            else: print ("Error")
        elif choose == 3:
            tmp = queue.front()
            if tmp != -1: print ("First element:",tmp)
            else: print ("Error")
        elif choose == 4:
            print(queue.isEmpty())
        elif choose == 5:
            print ("Size:",queue.size())
        elif choose == 6:
            queue.display()
        elif choose == 7:
            queue.clear()
        else:
            print("Input WRONG!")

if __name__ == '__main__':
    queue = Queue()
    menu(queue)
