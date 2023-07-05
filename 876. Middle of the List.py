# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        n = 0
        while head:
            head = head.next
            n+=1
        for _ in range(n//2):
            root =root.next
        return root
