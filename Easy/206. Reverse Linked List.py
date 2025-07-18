# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:
            return head
        prev=None
        curr=head
        nexT=head.next
        while curr!=None:
            curr.next=prev
            prev=curr
            curr=nexT
            if nexT!=None:
               nexT=nexT.next
        head=prev
        return head
