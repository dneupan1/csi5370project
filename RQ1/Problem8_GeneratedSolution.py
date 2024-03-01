class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    # Helper function to reverse a portion of the list
    def reverse(head, k):
        prev, curr = None, head
        for _ in range(k):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev, head  # New head and tail after reversal
    
    # Check if the list has at least k nodes
    count = 0
    ptr = head
    while count < k and ptr:
        ptr = ptr.next
        count += 1
    
    # If we have at least k nodes, proceed with reversal
    if count == k:
        # Reverse the first k nodes
        new_head, new_tail = reverse(head, k)
        
        # Recursively call for the rest of the list and connect them
        new_tail.next = reverseKGroup(ptr, k)
        
        return new_head
    return head

# Note: This code snippet assumes the existence of a linked list structure and does not include code for list creation or display.
