import pytest
from Problem8_GeneratedSolution import reverseKGroup, ListNode  # Adjust the import path as needed

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

def test_list_length_multiple_of_k():
    """
    Test a list length that is a multiple of k.
    """
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    k = 2
    expected = [2, 1, 4, 3, 6, 5]
    assert linked_list_to_array(reverseKGroup(head, k)) == expected, "Should reverse every k group of nodes"

def test_list_length_not_multiple_of_k():
    """
    Test a list length that is not a multiple of k, leaving the remainder as is.
    """
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 3
    expected = [3, 2, 1, 4, 5]
    assert linked_list_to_array(reverseKGroup(head, k)) == expected, "Should reverse the first k group of nodes and leave the rest as is"

def test_list_shorter_than_k():
    """
    Test a list that is shorter than k.
    """
    head = create_linked_list([1, 2])
    k = 3
    expected = [1, 2]
    assert linked_list_to_array(reverseKGroup(head, k)) == expected, "Should leave the list as is if shorter than k"

def test_k_equals_one():
    """
    Test with k equals 1, which should leave the list as is.
    """
    head = create_linked_list([1, 2, 3, 4])
    k = 1
    expected = [1, 2, 3, 4]
    assert linked_list_to_array(reverseKGroup(head, k)) == expected, "Should leave the list as is if k is 1"

def test_empty_list():
    """
    Test an empty list.
    """
    head = create_linked_list([])
    k = 2
    expected = []
    assert linked_list_to_array(reverseKGroup(head, k)) == expected, "Should return an empty list"

def test_single_node_list():
    """
    Test a list with a single node.
    """
    head = create_linked_list([1])
    k = 2
    expected = [1]
    assert linked_list_to_array(reverseKGroup(head, k)) == expected, "Single-node list should remain unchanged"
