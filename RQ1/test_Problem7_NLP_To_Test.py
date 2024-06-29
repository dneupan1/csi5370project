class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize the ListNode with a value and a pointer to the next node.
        :param val: Value of the node
        :param next: Pointer to the next node
        """
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    """
    This function swaps every two adjacent nodes in a linked list and returns the head of the modified list.
    
    :param head: The head of the linked list
    :return: The head of the modified linked list with swapped nodes
    """
    # Dummy node to handle edge cases such as empty list or single node list
    dummy = ListNode(0)
    dummy.next = head
    # Initialize a pointer to traverse the list
    current = dummy

    # Traverse the list while there are at least two more nodes to swap
    while current.next and current.next.next:
        # Identify the two nodes to be swapped
        first = current.next
        second = current.next.next

        # Swap the nodes
        first.next = second.next
        second.next = first
        current.next = second

        # Move the pointer forward by two nodes for the next pair
        current = first

    # Return the new head of the list
    return dummy.next

# Helper function to convert a list to a linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst