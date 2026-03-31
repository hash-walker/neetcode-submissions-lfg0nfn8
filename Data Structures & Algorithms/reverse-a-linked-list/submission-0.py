# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        reverse_arr = []

        while cur:
            reverse_arr.append(cur.val)
            cur = cur.next

        cur = head

        while cur:
            cur.val = reverse_arr.pop()
            cur = cur.next
        
        return head
        
        

        