# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head 
        for _ in range(n):
            first = first.next
        if first is None:
            return head.next
        while first.next:
            first, second = first.next, second.next
        second.next = second.next.next
        return head