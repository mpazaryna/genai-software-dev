"""
loop_examples.py

This module demonstrates the use of loops in Python. It includes examples of `for` loops and `while` loops, 
and provides functions that utilize these loops to perform various tasks. 

Additionally, pytest functions are included to test the functionality of these loop functions.

Explanation of Loops in Python

In Python, loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or 
other iterable objects. There are two main types of loops in Python:

- for loop: Iterates over a sequence of elements.
- while loop: Repeats as long as a certain condition is true.

"""


def sum_of_list(numbers):
    """
    Calculate the sum of all elements in a list using a for loop.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The sum of the numbers in the list.
    """
    total = 0
    for number in numbers:
        total += number
    return total


def find_first_even(numbers):
    """
    Find the first even number in a list using a while loop.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The first even number in the list, or None if no even number is found.
    """
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            return numbers[index]
        index += 1
    return None


def count_down(start):
    """
    Count down from a given number to zero using a while loop.

    Args:
        start (int): The starting number.

    Returns:
        list: A list of numbers counting down to zero.
    """
    result = []
    while start >= 0:
        result.append(start)
        start -= 1
    return result
