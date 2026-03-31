# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_ptr = head
        prev_ptr = None

        while cur_ptr:
            next_ptr = cur_ptr.next
            cur_ptr.next = prev_ptr
            prev_ptr = cur_ptr
            cur_ptr = next_ptr
        
        return prev_ptr