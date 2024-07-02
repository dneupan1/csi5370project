import pytest
from Problem7_GeneratedSolution import swapPairs, ListNode  # Adjust the import path as needed

def create_linked_list(arr):
    """Utility function to create a linked list from an array."""
    head = ListNode(arr[0]) if arr else None
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_array(head):
    """Utility function to convert a linked list back to an array for easy comparison."""
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

def test_empty_list():
    """
    Test swapping pairs in an empty list.
    """
    assert linked_list_to_array(swapPairs(create_linked_list([]))) == [], "Empty list should remain unchanged"

def test_single_node_list():
    """
    Test swapping pairs in a list with a single node.
    """
    assert linked_list_to_array(swapPairs(create_linked_list([1]))) == [1], "Single-node list should remain unchanged"

def test_even_number_of_nodes():
    """
    Test swapping pairs in a list with an even number of nodes.
    """
    assert linked_list_to_array(swapPairs(create_linked_list([1, 2, 3, 4]))) == [2, 1, 4, 3], "Pairs should be swapped in a list with an even number of nodes"

def test_odd_number_of_nodes():
    """
    Test swapping pairs in a list with an odd number of nodes.
    """
    assert linked_list_to_array(swapPairs(create_linked_list([1, 2, 3, 4, 5]))) == [2, 1, 4, 3, 5], "Pairs should be swapped with the last node remaining in place in a list with an odd number of nodes"

