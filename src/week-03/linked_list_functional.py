"""
Functional Linked List Implementation

This module demonstrates the concept of a linked list data structure in Python
using a functional programming approach.

In this implementation, we use immutable tuples to represent nodes and pure functions
for operations on the linked list. This approach aligns with functional programming
principles, emphasizing immutability and avoiding side effects.

Downsides and Overhead of Using Linked Lists (Functional Approach):

1. Immutability Overhead:
   - Each operation that modifies the list creates a new list, potentially leading
     to increased memory usage, especially for large lists.
   - This can result in performance overhead for frequent modifications.

2. Recursion-Heavy:
   - Many operations in a functional linked list rely on recursion, which can lead
     to stack overflow errors for very large lists.
   - Recursion may also be less intuitive for developers used to imperative styles.

3. Memory Usage:
   - As with OOP linked lists, each node requires extra memory for storing the
     reference to the next node.
   - In the functional approach, creating new lists for modifications can temporarily
     increase memory usage.

4. Random Access Inefficiency:
   - Accessing elements by index remains O(n) time complexity, requiring traversal
     from the beginning of the list.

5. Lack of Traditional Optimization Techniques:
   - Some optimizations available in imperative programming (like tail-call optimization)
     may not be available or as effective in all Python implementations.

6. Potential for Decreased Readability:
   - For developers more familiar with imperative or OOP styles, functional linked
     lists might be less intuitive and harder to read or maintain.

7. Limited Standard Library Support:
   - Python's standard library is not optimized for functional programming patterns,
     which may limit the interoperability of this implementation with built-in functions.

Despite these downsides, functional linked lists can offer benefits such as easier
reasoning about code behavior, natural support for persistent data structures,
and potentially simpler parallel processing of list operations.
"""

from functools import reduce
from typing import Any, Optional, Tuple

# Type alias for our linked list node
Node = Tuple[Any, Optional["Node"]]


def empty() -> Optional[Node]:
    """
    Create an empty linked list.

    Returns:
        None, representing an empty list.
    """
    return None


def cons(data: Any, rest: Optional[Node]) -> Node:
    """
    Construct a new list by prepending a new node to an existing list.

    Args:
        data: The data for the new node.
        rest: The rest of the list (can be None for a single-element list).

    Returns:
        A new Node representing the head of the new list.
    """
    return (data, rest)


def head(lst: Node) -> Any:
    """
    Get the data from the first node of the list.

    Args:
        lst: The linked list.

    Returns:
        The data from the first node.

    Raises:
        ValueError: If the list is empty.
    """
    if lst is None:
        raise ValueError("Empty list")
    return lst[0]


def tail(lst: Node) -> Optional[Node]:
    """
    Get the rest of the list (all nodes except the first one).

    Args:
        lst: The linked list.

    Returns:
        The rest of the list, or None if the list is empty or has only one element.
    """
    if lst is None:
        return None
    return lst[1]


def is_empty(lst: Optional[Node]) -> bool:
    """
    Check if the list is empty.

    Args:
        lst: The linked list.

    Returns:
        True if the list is empty, False otherwise.
    """
    return lst is None


def length(lst: Optional[Node]) -> int:
    """
    Calculate the length of the list.

    Args:
        lst: The linked list.

    Returns:
        The number of nodes in the list.
    """

    def length_acc(l: Optional[Node], acc: int) -> int:
        return acc if is_empty(l) else length_acc(tail(l), acc + 1)

    return length_acc(lst, 0)


def append(lst: Optional[Node], data: Any) -> Node:
    """
    Append a new node to the end of the list.

    Args:
        lst: The linked list.
        data: The data for the new node.

    Returns:
        A new list with the new node appended.
    """
    if is_empty(lst):
        return cons(data, None)
    return cons(head(lst), append(tail(lst), data))


def map_list(func: callable, lst: Optional[Node]) -> Optional[Node]:
    """
    Apply a function to each element of the list.

    Args:
        func: The function to apply to each element.
        lst: The linked list.

    Returns:
        A new list with the function applied to each element.
    """
    if is_empty(lst):
        return None
    return cons(func(head(lst)), map_list(func, tail(lst)))


def filter_list(pred: callable, lst: Optional[Node]) -> Optional[Node]:
    """
    Filter the list, keeping only elements that satisfy the predicate.

    Args:
        pred: The predicate function.
        lst: The linked list.

    Returns:
        A new list containing only elements that satisfy the predicate.
    """
    if is_empty(lst):
        return None
    if pred(head(lst)):
        return cons(head(lst), filter_list(pred, tail(lst)))
    return filter_list(pred, tail(lst))


def to_list(lst: Optional[Node]) -> list:
    """
    Convert the linked list to a Python list.

    Args:
        lst: The linked list.

    Returns:
        A Python list containing the elements of the linked list.
    """

    def to_list_acc(l: Optional[Node], acc: list) -> list:
        return acc if is_empty(l) else to_list_acc(tail(l), acc + [head(l)])

    return to_list_acc(lst, [])


def from_list(lst: list) -> Optional[Node]:
    """
    Create a linked list from a Python list.

    Args:
        lst: A Python list.

    Returns:
        A linked list containing the elements from the Python list.
    """
    return reduce(lambda acc, x: cons(x, acc), reversed(lst), None)


def display(lst: Optional[Node]) -> str:
    """
    Create a string representation of the list.

    Args:
        lst: The linked list.

    Returns:
        A string representation of the list.
    """
    return " -> ".join(map(str, to_list(lst))) + " -> None"


# Example usage
if __name__ == "__main__":
    # Create a list: 5 -> 2 -> 1 -> 4
    my_list = cons(5, cons(2, cons(1, cons(4, None))))
    print("Original list:")
    print(display(my_list))

    # Append 6 to the list
    my_list = append(my_list, 6)
    print("\nAfter appending 6:")
    print(display(my_list))

    # Map: multiply each element by 2
    doubled = map_list(lambda x: x * 2, my_list)
    print("\nAfter doubling each element:")
    print(display(doubled))

    # Filter: keep only even numbers
    evens = filter_list(lambda x: x % 2 == 0, my_list)
    print("\nKeeping only even numbers:")
    print(display(evens))

    # Length of the list
    print(f"\nLength of the original list: {length(my_list)}")

    # Convert to and from Python list
    python_list = to_list(my_list)
    print(f"\nAs Python list: {python_list}")
    back_to_linked = from_list(python_list)
    print("Back to linked list:")
    print(display(back_to_linked))
