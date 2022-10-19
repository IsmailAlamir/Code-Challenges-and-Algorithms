# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def delete(self,value):
        current=self.head
        previus=None
        while current.value != value:
            previus=current
            current=current.next
        
        previus.next=current.next  
        current=None
    

    def printAll(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next