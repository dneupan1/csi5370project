class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize the ListNode with a value and a pointer to the next node.
        :param val: Value of the node
        :param next: Pointer to the next node
        """
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    """
    This function reverses the nodes of the linked list k at a time and returns the modified list.
    
    :param head: The head of the linked list
    :param k: The number of nodes to reverse at a time
    :return: The head of the modified linked list
    """
    
    def reverseLinkedList(head: ListNode, k: int) -> ListNode:
        """
        This helper function reverses k nodes of the linked list.
        :param head: The head of the part of the linked list to be reversed
        :param k: The number of nodes to reverse
        :return: The new head of the reversed linked list part
        """
        new_head, ptr = None, head
        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head
    
    # Dummy node to handle edge cases such as empty list
    dummy = ListNode(0)
    dummy.next = head
    
    # Pointer to traverse the list
    group_prev = dummy
    
    while True:
        # Check if there are at least k nodes left to reverse
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        
        # Store the next group's start node
        group_next = kth.next
        
        # Reverse the k nodes
        prev, curr = group_prev.next, group_prev.next.next
        for _ in range(k - 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Adjust the pointers to connect with the previous part of the list
        temp = group_prev.next
        group_prev.next = prev
        temp.next = group_next
        
        # Move the group_prev pointer for the next group of k nodes
        group_prev = temp

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
