# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        count = 0

        while (curr):
            count +=1
            curr = curr.next

        index = count - n

        if index == 0 and count == 1:
            return None
        elif index == 0 and count > 1:
            return head.next

        curr = head
        prev = None
        
        while ( index > 0 and curr):
            prev = curr
            curr = curr.next
            index -= 1
        
        prev.next = curr.next
        return head
            