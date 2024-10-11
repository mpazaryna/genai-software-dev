"""
Linked List Implementation

This module demonstrates the concept of a linked list data structure in Python.

A linked list is a linear data structure where elements are stored in nodes. Each node
contains a data field and a reference (link) to the next node in the sequence.

Downsides and Overhead of Using Linked Lists:

1. Memory Overhead:
   - Each node in a linked list requires extra memory for storing the reference to the
     next node, which is not needed in array-based structures.
   - This additional memory usage can be significant for large lists, especially when
     storing small data items.

2. Random Access Inefficiency:
   - Accessing elements by index is O(n) time complexity, as you need to traverse the
     list from the beginning to reach a specific index.
   - This makes linked lists inefficient for applications requiring frequent random access.

3. Cache Unfriendliness:
   - Linked list nodes are typically scattered in memory, leading to poor cache performance
     compared to contiguous array-based structures.
   - This can result in slower overall performance, especially for large lists.

4. Extra Code Complexity:
   - Implementing and maintaining linked lists often requires more complex code compared
     to array-based structures, especially for operations like insertion and deletion.

5. Reverse Traversal Difficulty:
   - In a singly linked list, reverse traversal is not possible without additional
     modifications or keeping track of previous nodes.

6. Higher Risk of Memory Leaks:
   - Improper management of node references can lead to memory leaks, especially in
     languages without automatic garbage collection.

7. Additional Time Overhead:
   - Operations like insertion and deletion, while O(1) at a known position, require
     traversal to find the position, making them O(n) in practice for arbitrary positions.

Despite these downsides, linked lists can be beneficial in scenarios requiring frequent
insertions and deletions at the beginning or middle of the list, or when the size of the
list is unknown and needs to grow dynamically.
"""


class Node:
    """
    Represents a node in the linked list.

    Each node contains a data item and a reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a new node.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Implements a singly linked list.

    This class provides methods for basic linked list operations such as
    insertion, deletion, and traversal.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.

        Args:
            data: The data to be inserted.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.

        Args:
            data: The data to be inserted.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        """
        Delete the first occurrence of a node with the given key.

        Args:
            key: The data to be deleted.
        """
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def display(self):
        """
        Display the contents of the linked list.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    llist = LinkedList()

    llist.insert_at_end(1)
    llist.insert_at_beginning(2)
    llist.insert_at_beginning(3)
    llist.insert_at_end(4)
    llist.insert_at_beginning(5)

    print("Linked List:")
    llist.display()

    print("\nDeleting 3:")
    llist.delete_node(3)
    llist.display()

    print("\nDeleting 5:")
    llist.delete_node(5)
    llist.display()
