class Node:
    def __init__(self, value, prevNode = None, nextNode = None): # constructor to add a new node
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode

class Doubly_LinkedList: 
    def __init__(self, head = None): # Constructor for empty dll
        self.head = head
    
    def push(self, new_data): #inserting a node at the front of the dll
        new_node = Node(value = new_data)
        new_node.nextNode = self.head
        new_node.prevNode = None
    
        if self.head is not None:
            self.head.prevNode = new_node
        
        self.head = new_node

    def insertAfter(self, prevNode, new_data):
        if prevNode is None:
            print('this node does not exist')
            return
        new_node = Node(value = new_data)
        new_node.nextNode = prevNode.nextNode # make next of the new mode as next of prev node
        prevNode.nextNode = new_node
        new_node.prevNode = prevNode
        if new_node.nextNode is not None: # Change previous of new nodes next node
            new_node.nextNode.prevNode = new_node

    def append(self, new_data): # add a node at the end
        new_node = Node(value = new_data)
        last = self.head
        new_node.nextNode = None
        if self.head is None: # if dll is empty, make the new node as head
            new_node.prevNode = None
            self.head = new_node
            return

        while last.nextNode is not None: # traverse/iterate through the list
            last = last.nextNode
        
        last.nextNode = new_node # we change the next of the last node to the new node 
        new_node.prevNode = last # we change the previous of the new last node to the old last node
        
    def printllist(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.nextNode
        print('None')

llist = Doubly_LinkedList()
llist.printllist()
llist.append([6, 7, 8])
llist.printllist()
llist.push(9)
llist.printllist()        
    
            