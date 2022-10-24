# Write here the code challenge solution
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

    def middleNode(self, head): 
        # get_middle method return the middle node of the linked list       
        node_value=[]
        while head is not None:
            node_value.append(head.value) 
            head=head.next
        return node_value[len(node_value)//2:]

    def printAll(self):
        # printAll method print and return new list 
        # and if the linked list is empty it return empty linked list

        list_of_node=[]
        if self.head is None :
            return "empty linked list"
        else :
            current = self.head
            while current is not None:
                list_of_node.append(current.value)
                current = current.next
        return list_of_node





def delete(node):
# delete function is a function that take the node and delete it from the linked list 
    nextNode = node.next
    node.value = nextNode.value
    node.next = nextNode.next

