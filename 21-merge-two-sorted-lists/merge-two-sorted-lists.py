# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print (list1)
        print(list2)

        start = None
        curr = None
        temp = None
        
        if list2 == None:
            return list1
        elif list1 == None:
            return list2

        if list1.val < list2.val:
            start = list1
            curr = start
            list1 = list1.next
        else:
            start = list2
            curr = start
            list2 = list2.next
        
        while (curr != None):
            if list1 == None:
                curr.next = list2
                break
            elif list2 == None:
                curr.next = list1
                break

            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        return start