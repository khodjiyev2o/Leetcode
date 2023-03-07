class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Create a dummy node to simplify the logic
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # Move the fast pointer n nodes ahead of the slow pointer
    for _ in range(n):
        fast = fast.next

    # Move both pointers together until the fast pointer reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Remove the nth node from the end by linking the slow node to its next next node
    slow.next = slow.next.next

    return dummy.next
