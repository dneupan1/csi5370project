class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    # Step 0: Handle the edge case of an empty list
    if not head or not head.next:
        return head

    # Step 1: Initialize a dummy node and a prev pointer to help with swapping
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy

    # Step 2: Iterate through the list and swap pairs
    while prev.next and prev.next.next:
        # Identify the nodes to be swapped
        first = prev.next
        second = first.next
        
        # Swapping process
        prev.next = second
        first.next = second.next
        second.next = first
        
        # Move prev two steps forward for the next swap
        prev = first

    # Step 3: Return the new head of the list
    return dummy.next
