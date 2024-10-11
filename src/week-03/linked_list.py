import threading


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, max_size=None):
        self.head = None
        self.size = 0
        self.max_size = max_size  # Maximum size limit for the linked list
        self.lock = threading.Lock()  # Lock for concurrency control

    def append(self, data):
        # Validate input data
        if (
            len(data) > 1000
        ):  # Example: Limit data size to prevent excessively large payloads
            raise ValueError("Data size exceeds maximum limit")

        with self.lock:
            # Rate limiting mechanism can be implemented here
            if self.max_size is not None and self.size >= self.max_size:
                raise ValueError("Linked list is full")

            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                last = self.head
                while last.next:
                    last = last.next
                last.next = new_node
            self.size += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def remove(self, data):
        """
        Removes the first occurrence of a node containing the specified data from the linked list.

        Parameters:
        data (any): The data value to be removed from the linked list.

        Raises:
        ValueError: If the data is not found in the linked list.

        This method uses a lock to ensure thread safety during the removal process. It traverses the list
        to find the node with the specified data. If found, it adjusts the pointers to exclude the node
        from the list and decrements the size of the list. If the data is not found, a ValueError is raised.
        """
        with self.lock:
            current = self.head
            previous = None

            while current:
                if current.data == data:
                    if previous is None:
                        self.head = current.next
                    else:
                        previous.next = current.next
                    self.size -= 1
                    return
                previous = current
                current = current.next

            raise ValueError("Data not found in the linked list")


# Example usage
list = LinkedList(max_size=1000)  # Set maximum size limit
list.append("Data 1")
list.append("Data 2")
list.print_list()
print("\nRemoving 'Data 1'")
list.remove("Data 1")
list.print_list()
