# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next

        temp = ListNode(0)
        temp.next = head
        prev = temp
        curr = head

        for _ in range(length//k):
            for _ in range(k-1):
                nextNode = curr.next
                curr.next = nextNode.next
                nextNode.next = prev.next
                prev.next = nextNode

            prev = curr
            curr = curr.next
        
        return temp.next
