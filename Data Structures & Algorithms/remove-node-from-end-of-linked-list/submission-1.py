# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,fast = head,head
        while n:
            fast = fast.next
            n -=1

        if slow == fast or not fast:
            return head.next
        while fast and  fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head
        

