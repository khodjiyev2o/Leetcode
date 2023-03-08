class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def test_middleNode():
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Test with odd-length list
    assert middleNode(head).val == 3

    # Add another node: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head.next.next.next.next.next = ListNode(6)

    # Test with even-length list
    assert middleNode(head).val == 4

test_middleNode()

