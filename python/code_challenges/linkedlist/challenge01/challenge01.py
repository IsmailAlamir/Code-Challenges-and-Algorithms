# Write here the code challenge solution
class Node:
    #Node class to make a node and it take a value for the node
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    #LinkedList class have method for append and get
    def __init__(self):
        self.head = None
    
    def append(self, node):
    #append method take a node and put it in the Linked List
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            
    def get(self,value):
    #get method value for node and get it 
        current=self.head
        while current.value != value:
            current=current.next
        return current


    # def delete(self,value):
    #     current=self.head
    #     previus=None
    #     while current.value != value:
    #         previus=current
    #         current=current.next
        
    #     previus.next=current.next  
    #     current=None
    

    def printAll(self):
        # printAll method print and return new list 
        # and if the linked list is empty it return empty linked list

        list_of_node=[]
        if self.head is None :
            print("empty linked list")
        else :
            current = self.head
            while current is not None:
                list_of_node.append(current.value)
                print(current.value)

                current = current.next
        print(list_of_node)
        return list_of_node





def delete(node):
# delete function is a function that take the node and delete it from the linked list 
    nextNode = node.next
    node.value = nextNode.value
    node.next = nextNode.next