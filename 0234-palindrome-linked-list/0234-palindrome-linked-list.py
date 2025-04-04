# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True