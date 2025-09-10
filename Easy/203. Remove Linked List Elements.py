# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if head==None:
            return head
        if head.next==None and head.val==val:
            head=None
            return head  
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy      
        curr=head
        nexT=curr.next
        while curr is not None:
            if curr.val==val:
                prev.next=nexT
                curr=nexT
                if nexT is not None:
                    nexT=nexT.next
                if curr is None:
                    return dummy.next
            else:
                prev=curr
                curr=nexT
                if nexT is not None:
                    nexT=nexT.next
        return dummy.next            

                


        
