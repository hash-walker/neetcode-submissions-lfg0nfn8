# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow ,fast = head,head.next
        #find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first ,second = head,prev

        while second:
            tmp1,tmp2 = first.next,second.next
            second.next = tmp1
            first.next = second
            first = tmp1
            second = tmp2

        
                

        



