# Main Concept of Doubly Linked Lists

Each Element of a linked list is called a node, and every node has three different fields:
1. Data contains the value to be stored in the node
2. Next contains a reference to the next node on the list
3. Prev contains a reference to the previous node on the list

A linked list is a collection of nodes. 
First node is called head, and it's used as the starting point for any iteration through the list.
Last node must have it's next reference pointing to None to determine the end of the list


## Doubly Linked Lists vs. Singly Linked Lists:

### Memory usage 
- As singly linked list store pointer of only one node so consumes lesser memory.
- On other hand Doubly linked list uses more memory per node(two pointers).

### Internal Implementation
- In singly linked list implementation is such as where the node contains some data and a pointer to the next node in the list
- While doubly linked list has some more complex implementation where the node contains some data and a pointer to the next as well as the previous node in the list

### Order of elements
- Singly linked list allows traversal elements only in one way.
- Doubly linked list allows element two way traversal.

### Usage
- Singly linked list are generally used for implementation of stacks
- On other hand doubly linked list can be used to implement stacks as well as heaps and binary trees.

### Performance
- In order to delete a node and connect the previous and the next node together, you need to know their pointers. In a doubly-linked list, both pointers are available in the node that is to be deleted. The time complexity is constant in this case, i.e., O(1).
- Whereas in a singly-linked list, the pointer to the previous node is unknown and can be found only by traversing the list from head until it reaches the node that has a next node pointer to the node that is to be deleted. The time complexity in this case is O(n).

![ImgName](https://github.com/KarimsHub/Doubly_linked_list_datastructure/blob/master/sllvsdll.jpg?raw=true)

