import pytest
from Problem8_GeneratedSolution import ListNode
from Problem8_GeneratedSolution import reverseKGroup as reverse_k_group  # Assuming the reverse function is defined in solution.py

class TestReverseKGroup:
    @staticmethod
    def build_linked_list(values):
        """ Helper function to construct a linked list from a list of integers. """
        dummy = ListNode(0)  # Dummy node to handle edge cases more uniformly
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next  # Return the node following the dummy, which is the head of the actual list

    @staticmethod
    def extract_values(head):
        """ Helper function to extract values from a linked list into a list. """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

    @pytest.mark.parametrize("values, k, expected", [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([], 1, []),
        ([1], 1, [1]),
        ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
        ([1, 2, 3, 4, 5, 6], 4, [4, 3, 2, 1, 5, 6]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [5, 4, 3, 2, 1, 6, 7, 8, 9])
    ])
    def test_reverse_k_group(self, values, k, expected):
        """
        Tests the `reverse_k_group` function with various lists and values of k.
        Validates that the function correctly reverses nodes in groups of k and
        leaves remaining nodes as is when not enough to form a complete group.
        """
        head = self.build_linked_list(values)
        reversed_head = reverse_k_group(head, k)
        result = self.extract_values(reversed_head)
        assert result == expected, f"Expected {expected}, got {result}"

# This script uses a class structure to encapsulate helper methods and test cases,
# providing a clean and organized way to test the linked list reversal function.
