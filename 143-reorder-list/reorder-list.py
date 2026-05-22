# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        seen = []

        while (curr):
            seen.append(curr)
            curr = curr.next
        
        l, r = 0, len(seen)-1

        while l < r:
            seen[l].next = seen[r]
            l += 1
            if (l >= r):
                break
            seen[r].next = seen[l]
            r -= 1
        
        seen[l].next = None

        return (seen[0])