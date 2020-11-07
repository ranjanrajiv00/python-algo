import node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        newNode = node.Node(data)

        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def display(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

linkedList = LinkedList()
linkedList.insert(10)
linkedList.insert(20)
linkedList.insert(30)
linkedList.insert(40)
linkedList.insert(50)

linkedList.display()