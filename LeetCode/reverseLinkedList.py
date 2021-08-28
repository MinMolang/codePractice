# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution ref. moby
class Solution:
    def reverseList_V1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
    
        # recursive
    def reverseList(self, head):
        """
        :type head : ListNode
        :rtype : ListNode
        """
        if not head or not head.next: # ListNode{val: 5, next: None}
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
        
# head :: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
# expected :: ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}
    
        
