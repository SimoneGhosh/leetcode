# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find half way
        slow = head
        fast = head.next

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd hald
        prev = None
        curr = slow.next
        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reverse = prev
        slow.next = None

        # combine both
        new = head

        while (head and reverse):
            temp = head.next
            head.next = reverse
            reverse = reverse.next
            head = head.next
            head.next = temp
            head = head.next
        
        if (reverse):
            head.next = reverse

        return (new)
        