# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        currNode = head
        nextNode = head.next
        currNode.next = None
        while nextNode:
            temp = nextNode.next
            nextNode.next = currNode
            currNode = nextNode
            nextNode = temp
        return currNode




