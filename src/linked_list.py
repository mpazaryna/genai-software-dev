class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    LinkedList implementation with basic operations and DoS mitigation features.

    Points of Interest:
    1. Input Validation: Ensures only valid data is appended to the list.
    2. Size Tracking: Keeps track of the number of elements in the list.
    3. Clear Method: Provides a way to reset the list, aiding in resource management.
    4. Get Size Method: Allows retrieval of the current size of the list.
    """

    def __init__(self):
        self.head = None
        self.size = 0  # Track the size of the list

    def append(self, data):
        # Input validation
        if not isinstance(data, str):
            raise ValueError("Only string data is allowed")

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1  # Increment size

    def remove(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size -= 1  # Decrement size
                return True
            previous = current
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def get_size(self):
        return self.size  # Return the size of the list

    def clear(self):
        self.head = None
        self.size = 0  # Reset size


# Example usage
linked_list = LinkedList()
linked_list.append("Alice")
linked_list.append("Bob")
linked_list.append("Charlie")
linked_list.display()
linked_list.remove("Bob")
linked_list.display()
print("Size of the list:", linked_list.get_size())
linked_list.clear()
print("Size of the list after clearing:", linked_list.get_size())
