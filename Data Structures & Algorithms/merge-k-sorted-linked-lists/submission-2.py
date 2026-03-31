# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:   
  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) //2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.mergeTwoLists(left, right)
        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        dummy = node = ListNode()
        while cur1 and cur2:
                if cur1.val <= cur2.val:
                    node.next = cur1
                    cur1 = cur1.next
                else:
                    node.next = cur2
                    cur2 = cur2.next
                
                node = node.next
        
        node.next = cur1 or cur2
        
        return dummy.next 