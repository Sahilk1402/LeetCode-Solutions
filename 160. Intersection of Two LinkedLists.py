# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        l1,l2 = 0,0
        curr1,curr2 = head1,head2

        while curr1:
            l1 +=1
            curr1 = curr1.next
        
        while curr2:
            l2 += 1
            curr2 = curr2.next

        if l1 > l2:
            for _ in range(l1-l2):
                head1 = head1.next
        elif l2 > l1:
            for _ in range(l2 -l1):
                head2 = head2.next

        while head1 and head2 is not None:
            if head1 == head2:
                return head1

            head1 = head1.next
            head2 = head2.next

        return None       
