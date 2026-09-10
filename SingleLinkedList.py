class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        element = []
        while current:
            element.append(str(current.data))
            current = current.next
        print("->".join(element))

    def reverse(self):
        previous = None
        current = self.head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous



mylist = SingleLinkedList()
mylist.append(10)
mylist.append(11)
mylist.append(12)
mylist.append(13)
mylist.display()
mylist.reverse()
mylist.display()
