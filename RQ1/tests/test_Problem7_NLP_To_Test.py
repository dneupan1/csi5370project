import pytest
from Problem7_GeneratedSolution import ListNode
from Problem7_GeneratedSolution import swapPairs as swap_pairs  # Assuming the swap function is defined in solution.py

def create_linked_list(values):
    """ Helper function to create a linked list from a list of values. """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    """ Helper function to convert a linked list to a list. """
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    return elements

@pytest.mark.parametrize("input_list, expected_output", [
    ([1, 2, 3, 4], [2, 1, 4, 3]),
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [2, 1, 3]),
    ([1, 2], [2, 1]),
    ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5])
])
def test_swap_pairs(input_list, expected_output):
    """
    Test the `swap_pairs` function to ensure it correctly swaps every two adjacent nodes in a linked list.
    """
    # Create linked list from input list
    head = create_linked_list(input_list)
    # Call the swap function
    swapped_head = swap_pairs(head)
    # Convert the result back to a list to verify correct order
    result_list = linked_list_to_list(swapped_head)
    # Assert the result matches the expected output
    assert result_list == expected_output, f"Failed for input {input_list}"

